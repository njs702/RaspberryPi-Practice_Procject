# import library
import time
import Adafruit_SSD1306
from PIL import Image, ImageDraw,ImageFont
import Adafruit_BMP.BMP085 as BMP085

# OLED 128 X 64 Instance disp create
disp = Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3c)

# disp initialize
disp.begin()

# display clear
disp.clear()
disp.display()

# Create blank image for drawing
# Make sure to create image with mode '1' for 1-bit color
width = disp.width
height = disp.height
image = Image.new('1',(width,height))

# Get drawing object to draw on image
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image
draw.rectangle((0,0,width,height),outline=0,fill=0)

#First define some constants to allow easy resizing of shapes
padding = -2
top = padding
bottom = height - padding

# Move left to right keeping track of the current x position for drawing shapes
x = 0

font = ImageFont.load_default()

# BMP180 sensor instance create
sensor = BMP085.BMP085()

while True:
	# temp, press, alti value save
	temp = sensor.read_temperature()
	pressure = sensor.read_pressure()
	ALTitude = sensor.read_altitude()
	
	# print to terminal
	print('Temp = {0:0.2f} *C'.format(temp))
	print('Pressure = {0:0.2f} Pa'.format(pressure))
	print('ALTitude = {0:0.2f} m'.format(ALTitude))
	
	# print to OLED
	draw.text((x,top),'Temp = {0:0.2f} *C'.format(temp),font=font, fill=255)
	draw.text((x,top+8),'Pressure = {0:0.2f} Pa'.format(pressure),font=font, fill=255)
	draw.text((x,top+16),'ALTitude = {0:0.2f} m'.format(ALTitude),font=font, fill=255)
	
	
	# LED display
	disp.image(image)
	disp.display()
	time.sleep(2)
	
