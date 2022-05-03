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

int main(void){
	// printf("can hello!!\n");
	int s;
	int nBytes;
	struct sockaddr_can addr;
	struct can_frame frame;
	struct ifreq ifr;

	struct can_filter rfilter[1];
	rfilter[0].can_id   = 0x550;
	rfilter[0].can_mask = 0xFF0;

	// Create Socket
	if((s=socket(PF_CAN,SOCK_RAW,CAN_RAW)) < 0){
		perror("Socket");
		return 1;
	}

	/* Retrieve the interface index for the interface name
	   (can0, can1, vcan0, etc ... ) */
	strcpy(ifr.ifr_name,"vcan0");
	ioctl(s,SIOCGIFINDEX,&ifr);

	// Bind Socket to the CAN interface
	memset(&addr,0,sizeof(addr));
	addr.can_family = AF_CAN;
	addr.can_ifindex = ifr.ifr_ifindex;

	if (bind(s,(struct sockaddr *)&addr, sizeof(addr)) < 0){
		perror("Bind");
		return 1;
	}

	// Reading a frame
	nBytes = read(s,&frame,sizeof(struct can_frame));
	if (nBytes < 0){
		perror("Read");
		return 1;
	}

	printf("0x%03X {%d} ",frame.can_id,frame.can_dlc);
	
	for (int i=0;i < frame.can_dlc; i++){
		printf("%02X ",frame.data[i]);
	}

	printf("\r\n");
	
	setsockopt(s, SOL_CAN_RAW, CAN_RAW_FILTER, &rfilter, sizeof(rfilter));

	if (close(s) < 0) {
		perror("Close");
		return 1;
	}
}
