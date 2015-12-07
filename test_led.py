import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

def Blink(numTimes, speed):
    for i in range(0, numTimes):
        print ("Iteration times: " + str(i+1))
        GPIO.output(7, True)
        time.sleep(speed)
        GPIO.output(7, False)
        time.sleep(speed)
    print "Done"
    GPIO.cleanup()

iteration = int(raw_input("Times to blink: "))
speed     = float(raw_input("Length of each blink: "))

Blink(iteration, speed)
