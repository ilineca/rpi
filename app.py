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
    return str(temperature)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
