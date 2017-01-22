#led test
import RPi.GPIO as GPIO
import time

PIN0 = 29
PIN1 = 31
PIN2 = 33
PIN3 = 36
PIN4 = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN0, GPIO.OUT)
GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)
GPIO.setup(PIN3, GPIO.OUT)
GPIO.setup(PIN4, GPIO.OUT)

try:
    while True:
        GPIO.output(PIN0, False)
        GPIO.output(PIN1, False)
        GPIO.output(PIN2, False)
        GPIO.output(PIN3, False)
        GPIO.output(PIN4, False)
        time.sleep(0.5)	
        GPIO.output(PIN0, True)
        time.sleep(0.5)
        GPIO.output(PIN1, True)
        time.sleep(0.5)
        GPIO.output(PIN2, True)
        time.sleep(0.5)
        GPIO.output(PIN3, True)
        time.sleep(0.5)
        GPIO.output(PIN4, True)
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
