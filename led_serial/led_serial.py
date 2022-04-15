import serial

arduino = serial.Serial('/dev/ttyACM0',115200,timeout = 1)
# arduino.open()

y = arduino.readline()
if y != '':
    print(y.decode()[:-2])
        