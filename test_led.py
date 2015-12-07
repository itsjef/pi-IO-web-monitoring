import RPi.GPIO as GPIO
from notify.variable import * 
import time

PORT_I = 11
PORT_O = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(PORT_I, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(PORT_O, GPIO.OUT)

def Blink(numTimes, speed):
    for i in range(0, numTimes):
        print ("Iteration times: " + str(i+1))
        GPIO.output(PORT_O, True)
        time.sleep(speed)
        GPIO.output(PORT_O, False)
        time.sleep(speed)
    print "Done"
    GPIO.cleanup()

def print_state(state):
    print "HIGH" if state == GPIO.HIGH else "LOW"

def Flick():
    state = Variable()
    state.changed.connect(print_state)
    while True:
        try:
            state.value = GPIO.input(PORT_I)
        except:
            break
    GPIO.cleanup()

# Test output
# iteration = int(raw_input("Times to blink: ")) 
# speed     = float(raw_input("Length of each blink: "))
# Blink(iteration, speed)

# Test input
Flick()
