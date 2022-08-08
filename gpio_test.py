from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import datetime
from w1thermsensor import W1ThermSensor
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
sensor = W1ThermSensor()
temp_limit = 32
pin = 5
scheduler = BackgroundScheduler()
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, False)


@app.route("/")
def hello():
    now = datetime.datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M")
    template_data = {
        'title': 'HELLO!',
        'time': time_string
    }
    return render_template('main.html', **template_data)


@app.route("/set_temp/<temperature_limit>")
def set_limit_temperature(temperature_limit):
    global temp_limit
    temp_limit = int(temperature_limit)
    return temperature_limit


@app.route("/read_pin/<pin>")
def read_pin(pin):
    try:
        GPIO.setup(int(pin), GPIO.IN)
        response = GPIO.input(int(pin))
    except:
        response = "There was an error reading pin " + pin + ". Ops!"

    pin_data = {
        'title': 'Status of Pin' + pin,
        'response': response
    }

    return render_template('pin.html', template_data=pin_data)


@app.route("/read_output/<out_pin>")
def read_outpt_pin(out_pin):
    try:
        response = GPIO.output(int(pin))
    except:
        response = "There was an error reading pin " + pin + ". Ops!"

    pin_data = {
        'title': 'Status of Pin' + pin,
        'response': response
    }

    return render_template('pin.html', template_data=pin_data)


@app.route("/get_temp")
def get_temp():
    current_temperature = read_temperature()
    result_data = {
        'title': 'Status of temp:',
        'current_temperature': current_temperature
    }

    return render_template('main.html', template_data=result_data)


def read_temperature():
    return sensor.get_temperature()


def check_temperature():
    current_temperature = read_temperature()
    print(f"temperature: {current_temperature}")
    out_pin = GPIO.input(pin)
    print(f"Output pin: {out_pin}")
    if current_temperature >= temp_limit and (out_pin == 0):
        print(f"TEMP : {current_temperature} is above the limit {temp_limit}")
        GPIO.output(pin, True)
        print(f"GPIO PIN {pin} switched to True")
    elif current_temperature < temp_limit and (out_pin == 1):
        print(f"TEMP : {current_temperature} is below the limit {temp_limit}")
        GPIO.output(pin, False)
        print(f"GPIO PIN {pin} switched to False")


scheduler.add_job(func=check_temperature, trigger="interval", seconds=5)
scheduler.start()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
atexit.register(lambda: scheduler.shutdown())
