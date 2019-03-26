from flask import Flask, render_template
import datetime
from w1thermsensor import W1ThermSensor
import RPi.GPIO as GPIO
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

sensor = W1ThermSensor()


@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   return render_template('main.html', **templateData)

@app.route("/readPin/<pin>")
def readPin(pin):

    try:
        GPIO.setup(int(pin), GPIO.IN)
        response = GPIO.input(int(pin))
    except:
        response = "There was an error reading pin " + pin + ". Deeba!"

    templateData = {
      'title' : 'Status of Pin' + pin,
      'response' : response
      }

    return render_template('pin.html', **templateData)


@app.route("/getTemp")
def getTemp():
    response = sensor.aget_temperature()
    templateData = {
      'title' : 'Status of temp:',
      'response' : response
      }

    return render_template('pin.html', **templateData)



if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
