#-*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time

SERVO_PIN = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.OUT)

servo = GPIO.PWM(SERVO_PIN,50)

servo.start(0) # PWM 듀티비 0으로 시작

try:
	while True:
		servo.ChangeDutyCycle(7.5) #듀티비를 변경하여 특정 각도만큼 회전시킴 90도
		time.sleep(1)
		servo.ChangeDutyCycle(12.5) #듀티비를 변경하여 특정 각도만큼 회전시킴 180도
		time.sleep(1)
		servo.ChangeDutyCycle(2.5) #듀티비를 변경하여 특정 각도만큼 회전시킴 0도
		time.sleep(1)
except KeyboardInterrupt:
	servo.stop()
	GPIO.cleanup()
