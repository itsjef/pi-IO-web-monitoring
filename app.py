from flask import *
from flask_socketio import SocketIO, send, emit
import RPi.GPIO as GPIO

# Define constants
PIN_I = 11
PIN_O = 7

# Setup Flask app and SocketIO
app = Flask(__name__, static_url_path='/templates')
socketio = SocketIO(app)

# Setup GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Handle routes 
@app.route('/')
@app.route('/<pin>/<state>')
@app.route('/<state>')
def handle_state(pin=PIN_O, state="off"):
    try:
        GPIO.setup(pin, GPIO.OUT)
        if "on" == str(state):
            GPIO.output(pin, True)
        else:
            GPIO.output(pin, False)
        template = 'index.html'
    except:
        template = 'error.html'

    templateData = {
        'title' : 'Control pin #' + str(pin),
        'response' : 'Error reading pin #' + str(pin)
    }
    return render_template(template, **templateData)


# Input
@app.route('/read')
@app.route('/read/<pin>')
def readPin(pin=PIN_I):
    try:
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
        if GPIO.input(pin) == GPIO.HIGH:
            response = "Pin number " + str(pin) + " is high!"
        else:
            response = "Pin number " + str(pin) + " is low!"
        template = 'pin.html'
    except:
        response = "Error reading pin #" + str(pin)
        template = 'error.html'

    templateData = { 
        'title' : 'Monitor pin #' + str(pin),
        'response': response
    }
    return render_template(template, **templateData)

# run app
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
