from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

LED = 8
GPIO.setmode(GPIO.BOARD) # BOARD connector pin number
GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)

@app.route("/")
def helloworld():
    return "Hello World!"

@app.route("/led/on")
def led_on():
    GPIO.output(LED,GPIO.HIGH)
    return "LED ON"

@app.route("/gpio/cleanup")
def gpio_cleanup():
    GPIO.cleanup()
    return "GPIO CLEANUP"

@app.route("/led/off")
def led_off():
    GPIO.output(LED,GPIO.LOW)
    return "LED OFF"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
