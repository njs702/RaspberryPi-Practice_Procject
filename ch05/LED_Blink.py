#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

led_pin = 4 # GPIO 4
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM) # 약속된 GPIO 번호를 사용하는 것
GPIO.setup(led_pin,GPIO.OUT) # 출력으로 사용

for i in range(10):
	GPIO.output(led_pin,1) # High(3.3v) 출력
	time.sleep(1)
	GPIO.output(led_pin,0) # Low(0v) 출력
	time.sleep(1)

GPIO.cleanup()

