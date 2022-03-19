#-*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 센서에 연결한 핀 번호 설정
TRIG = 23
ECHO = 24

# TRIG와 ECHO 핀의 출렦 썰쩡
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

# TRIG핀의 출력을 0으로 설정
GPIO.output(TRIG,False)
print("Waiting for sensor to settle")

time.sleep(2)

try:
	while True:
		GPIO.output(TRIG,True) # TRIG 핀에 펄스신호를 만들기 위해 1 출력
		time.sleep(0.00001)
		GPIO.output(TRIG,False)
		
		while GPIO.input(ECHO)==0:
			start = time.time() # echo 핀 상승시간
		while GPIO.input(ECHO)==1:
			stop = time.time() # echo 핀 하강시간
			
		check_time = stop-start
		distance = check_time * 34300 / 2
		print("Distance : %.1f cm" %distance)
		time.sleep(0.4) # 0.4초 간격으로 센서 측정

except KeyboardInterrupt:
	print("Measurement stopped by user")
	GPIO.cleanup()
