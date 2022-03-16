#-*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.OUT)

p = GPIO.PWM(18,100)

Frq = [262,294,330,349,392,440,493,523]
speed = 1

p.start(10)

try:
	while 1:
		for fr in Frq:
			p.ChangeFrequency(fr)
			time.sleep(speed)
except KeyboardInterrupt:
	pass

p.stop()
GPIO.cleanup()
