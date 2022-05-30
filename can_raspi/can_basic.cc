#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#include <net/if.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/ioctl.h>

#include <linux/can.h>
#include <linux/can/raw.h>

/* ============== GLOBAL custom struct & union ============== */
typedef struct{
	float humid;
	float temp;
}temp_humid_data;

union temp_humid_union {
    temp_humid_data first;
    unsigned char second[8];
}; 
/* ========================================================== */



/* ============== GLOBAL variables ============== */
static temp_humid_data temp_humid;
static int can_socket; // CAN socket
static struct sockaddr_can addr;
static struct ifreq ifr; // ifreq structure contaning the interface name
/* ============================================== */



/* ============== GLOBAL functions ============== */
void init_bind_socket_can(){

	/* ======================  Create Socket using 3 parameters ======================
	domain/protocol family(PF_CAN), type of socket(raw or datagram),socket protocol */
	if((can_socket=socket(PF_CAN,SOCK_RAW,CAN_RAW)) < 0){
		perror("Socket");
		return;
	}

	/* Retrieve the interface index for the interface name(can0, can1, vcan0, etc ... ) */
	strcpy(ifr.ifr_name,"can0");

	/* 네트워크 관리 스택 접근을 위한 I/O controll, 사용자 영역에서 커널 영역의 데이터 접근(system call) using 3 parameters
	an open file descriptor(s), request code number(SIOCGIFINDEX), value */
	ioctl(can_socket,SIOCGIFINDEX,&ifr);

	// Bind Socket to the CAN interface
	memset(&addr,0,sizeof(addr));
	addr.can_family = AF_CAN;
	addr.can_ifindex = ifr.ifr_ifindex;

	if (bind(can_socket,(struct sockaddr *)&addr, sizeof(addr)) < 0){
		perror("Bind");
		return;
	}

	printf("CAN Socket creation & bind success!\n");
}
void init_bind_socket_tcp(){

}
/* ============================================== */



int main(void){
	
	int nBytes;
	//struct sockaddr_can addr;
	struct can_frame recieve_frame;
	struct can_frame send_frame;

	// ifreq structure contaning the interface name
	//struct ifreq ifr;

	struct can_filter rfilter[1];
	rfilter[0].can_id   = 0x550;
	rfilter[0].can_mask = 0xFF0;

	init_bind_socket_can();

	// Sending a frame
	send_frame.can_id = 0x12;
	send_frame.can_dlc = 8;
	
	for(int i=0;i<8;i++){
		send_frame.data[i] = i;
	}
	if (write(can_socket, &send_frame, sizeof(struct can_frame)) != sizeof(struct can_frame)) {
		perror("Write");
		return 1;
	}

	// Reading a frame
	nBytes = read(can_socket,&recieve_frame,sizeof(struct can_frame));
	if (nBytes < 0){
		perror("Read");
		return 1;
	}
	
	printf("0x%03X {%d} ",recieve_frame.can_id,recieve_frame.can_dlc);

	union temp_humid_union a;
	for (int i = 0; i < 8; ++i)
		a.second[i] = recieve_frame.data[i];

	printf("%f %f", a.first.humid, a.first.temp);
	printf("\r\n");

	setsockopt(can_socket, SOL_CAN_RAW, CAN_RAW_FILTER, &rfilter, sizeof(rfilter));

	if (close(can_socket) < 0) {
		perror("Close");
		return 1;
	}
}
