#stomp_sampler 2.0

import RPi.GPIO as GPIO
import time
from os import listdir
from os.path import isfile, join
from pyomx import Player

#globals
TOGGLEPLAY = 16
NEXT = 18
LED0 = 29
LED1 = 31
LED2 = 33
LED3 = 36
LED4 = 38
SAMPLESPATH = "samples"
BLINKSPEED = 0.5
DEBOUNCE = 1

#setup gpio
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TOGGLEPLAY, GPIO.IN)
GPIO.setup(NEXT, GPIO.IN)
GPIO.setup(LED0, GPIO.OUT)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)
GPIO.output(LED0, True)
GPIO.output(LED1, False)
GPIO.output(LED2, False)
GPIO.output(LED3, False)
GPIO.output(LED4, False)

leds = [LED0, LED1, LED2, LED3, LED4]
playbuttonstate = GPIO.input(TOGGLEPLAY)
nextbuttonstate = GPIO.input(NEXT)
print("waiting for input...")

def filenameatindex(index):
    fname = SAMPLESPATH + "/" + filenames[index]
    return fname

def setupplayer():
    global player
    global currenttrack
    
    nextfile = filenameatindex(currenttrack)
    player = Player(nextfile)
    print("ready to play: " + nextfile)

def updateleds():
    global player
    global leds
    global currenttrack
    
    #playing - blink
    if (player.paused == False):
        if (currenttrack < len(leds)):
            currentled = leds[currenttrack]
        else:
            currentled = leds[0]

        GPIO.output(currentled, False)
        time.sleep(BLINKSPEED)
        GPIO.output(currentled, True)
        time.sleep(BLINKSPEED)
        
    #paused - solid if current track
    else:
        if (currenttrack < len(leds)):
            for i in range(0, len(leds)):
                ledon = (i == currenttrack)
                led = leds[i]
                GPIO.output(led, ledon)
        else:
            led = leds[0]
            GPIO.output(led, True)

def nexttrack():
    global player
    global currenttrack
    
    player.stop()
        
    if (currenttrack + 1 < len(filenames)):
        currenttrack += 1
    else:
        currenttrack = 0
    setupplayer()

#read samples
currenttrack = 0
filenames = sorted(listdir(SAMPLESPATH))
setupplayer()

try:
    #runloop
    while True:

        player.pollDone()

        #play/pause button pressed - toggle play/pause state
        if GPIO.input(TOGGLEPLAY) != playbuttonstate:
            player.toggleplay()
            time.sleep(DEBOUNCE)
            playbuttonstate = GPIO.input(TOGGLEPLAY)
        #next track button pressed
        elif GPIO.input(NEXT) != nextbuttonstate:
            nexttrack()
            time.sleep(DEBOUNCE)
            nextbuttonstate = GPIO.input(NEXT)
        #otherwise, just update leds
        else:
            updateleds()   
        
except KeyboardInterrupt:
    print("goodbye")
    player.stop()
        
    GPIO.cleanup()
