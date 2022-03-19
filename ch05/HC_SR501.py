#-*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_R = 20
led_Y = 21
sensor = 17

# LED핀의 입출력 설정
GPIO.setup(led_R,GPIO.OUT)
GPIO.setup(led_Y,GPIO.OUT)
GPIO.setup(sensor,GPIO.IN)

print("PIR Ready. . .")
time.sleep(5) # PIR 센서 준비 시간


try:
	while True:
		state = 0
		state = GPIO.input(sensor)
		
		if state == 1: # 센서가 HIGH라면
			GPIO.output(led_Y,1) # 노란색 led 켬
			GPIO.output(led_R,0) # 빨간색 led 끔
			GPIO.input(sensor) == 0
			print("Motion Detected!")
			time.sleep(1)
		
		if state == 0:
			GPIO.output(led_Y,0)
			GPIO.output(led_R,1)
			time.sleep(1)
		state = 0
		
except keyboardInterrupt:
	Print("Stopped by User")
	GPIO.cleanup()
GPIO.cleanup()


"""
if GPIO.input(sensor) == 0: # 센서가 HIGH라면
	GPIO.output(led_Y,1) # 노란색 led 켬
	GPIO.output(led_R,0) # 빨간색 led 끔
	GPIO.input(sensor) == 0
	print("Motion Detected!")
	time.sleep(0.2)
		
if GPIO.input(sensor) == 1:
	GPIO.output(led_Y,0)
	GPIO.output(led_R,1)
	time.sleep(0.2)
	
GPIO.cleanup()
"""
