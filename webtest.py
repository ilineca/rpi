import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

while True:
    GPIO.output(24, True)
    time.sleep(1)
    GPIO.output(24, False)
    time.sleep(1)


import time
from w1thermsensor import W1ThermSensor
import RPi.GPIO as GPIO
sensor = W1ThermSensor()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, True)
while True:
    temperature = sensor.get_temperature()
    temp_f = (9 * temperature) / 5 + 32
    print("The temperature is %s Celsius or %s Fahrenheit" % (temperature, temp_f))
    if temperature > 30 :
        GPIO.output(24, False)
    else:
        GPIO.output(24, True)
    time.sleep(1)






from flask import Flask, render_template
from w1thermsensor import W1ThermSensor
import RPi.GPIO as GPIO
import time
app = Flask(__name__)

sensor = W1ThermSensor()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/test')
def test():
    temperature = sensor.get_temperature()
    return temperature;


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
