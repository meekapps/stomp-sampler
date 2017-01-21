#gpio button test

import RPi.GPIO as GPIO
import time

BUTTON0 = 16
BUTTON1 = 18

DEBOUNCE = 1

#setup gpio
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON0, GPIO.IN)
GPIO.setup(BUTTON1, GPIO.IN)
state0 = GPIO.input(BUTTON0)
state1 = GPIO.input(BUTTON1)

try:
    print(BUTTON0)
    print(BUTTON1)
    #runloop
    while True:
        if GPIO.input(BUTTON0) != state0:
            print("button 0 pressed")
            time.sleep(DEBOUNCE)
            state0 = GPIO.input(BUTTON0)
        elif GPIO.input(BUTTON1) != state1:
            print("button 1 pressed")
            time.sleep(DEBOUNCE)
            state1 = GPIO.input(BUTTON1)

except KeyboardInterrupt:
    GPIO.cleanup()
        
        
