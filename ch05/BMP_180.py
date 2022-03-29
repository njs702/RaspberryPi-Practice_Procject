#-*- coding: utf-8 -*-

# BMP 측정을 위한 라이브러리 호출
import Adafruit_BMP.BMP085 as BMP085

# BMP센서의 인스턴스 sensor 생성
sensor = BMP085.BMP085()

# 온도, 압력, 고도를 읽어서 변수에 저장
temp = sensor.read_temperature()
pressure = sensor.read_pressure()
ALTitude = sensor.read_altitude()

# 측정 값을 출력
print('Temp = {0:0.2f} *C'.format(temp))
print('Pressure = {0:0.2f} Pa'.format(pressure))
print('ALTitude = {0:0.2f} m'.format(ALTitude))
