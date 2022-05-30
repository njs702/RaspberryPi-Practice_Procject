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

#include <wiringPi.h>

#include <pthread.h>

int led_green = 23;
int led_blue = 24;

int btn_green = 20;
int btn_blue = 21;

/* ============== GLOBAL variables ============== */
static int can_socket; // CAN socket
static struct sockaddr_can addr;
static struct ifreq ifr; // ifreq structure contaning the interface name
/* ============================================== */

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

void* thread_func(void* arg){
    int nBytes;
    int csock = *((int*)arg);
    struct can_frame recieve_frame;

    nBytes = read(csock,&recieve_frame,sizeof(struct can_frame));
    if(nBytes < 0){
        perror("Read");
        return NULL;
    }

    switch(recieve_frame.can_id){
        case 0x90:
            printf("Green LED ON!\n");
            printf("0x%2X {%d} ",recieve_frame.can_id,recieve_frame.can_dlc);
            for(int i=0;i<recieve_frame.can_dlc;i++){
                printf("%X ",recieve_frame.data[i]);
            }
            printf("\r\n");
            digitalWrite(led_green,1);
            delay(500);
            digitalWrite(led_green,0);
            break;

        case 0x91:
            printf("Blue LED ON!\n");
            printf("0x%2X {%d} ",recieve_frame.can_id,recieve_frame.can_dlc);
            for(int i=0;i<recieve_frame.can_dlc;i++){
                printf("%X ",recieve_frame.data[i]);
            }
            printf("\r\n");
            digitalWrite(led_blue,1);
            delay(500);
            digitalWrite(led_blue,0);
            break;
        default:
            break;
    }
    
}

int main(){
    
    pthread_t thread;

    struct can_frame recieve_frame;
	struct can_frame send_frame;

    if(wiringPiSetupGpio()==-1){
        perror("wiringPiSetup");
        return 1;
    }

    init_bind_socket_can();

    pinMode(led_green,OUTPUT);
    pinMode(led_blue,OUTPUT);

    pinMode(btn_green,INPUT);
    pinMode(btn_blue,INPUT);

    while(1){
        pthread_create(&thread,NULL,thread_func,&can_socket);
        //pthread_join(thread,NULL);
    }


    if (close(can_socket) < 0) {
		perror("Close");
		return 1;
	}

}

