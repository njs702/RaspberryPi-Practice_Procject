#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

button_pin = 15

GPIO.setwarnings(False)

# GPIO 핀의 모드 설정
GPIO.setmode(GPIO.BCM)

# 버튼 핀의 입력설정, PULL DOWN 설정
GPIO.setup(button_pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

# 버튼 핀에 High 신호가 들오오면 출력
while 1:
	if GPIO.input(button_pin) == GPIO.HIGH:
		print("Button pushed!")
	time.sleep(0.1)
