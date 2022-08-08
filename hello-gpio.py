from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)


@app.route("/")
def hello():
    now = datetime.datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M")
    template_data = {
        'title': 'HELLO!',
        'time': time_string
    }
    return render_template('main.html', **template_data)


@app.route("/readPin/<pin>")
def readPin(pin):
    try:
        GPIO.setup(int(pin), GPIO.IN)
        response = GPIO.input(int(pin))
    except:
        response = "There was an error reading pin " + pin + ". Deeba!"

    templateData = {
        'title': 'Status of Pin' + pin,
        'response': response
    }

    '''
       try:
          GPIO.setup(int(pin), GPIO.IN)
          if GPIO.input(int(pin)) == True:
             response = "Pin number " + pin + " is high!!!"
          else:
             response = "Pin number " + pin + " is low!!!!"
       except:
          response = "There was an error reading pin " + pin + "."
    '''

    return render_template('pin.html', **templateData)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
