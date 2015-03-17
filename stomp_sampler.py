#stomp_sampler

import RPi.GPIO as GPIO
import time
from os import listdir
from os.path import isfile, join
from pyomx import Player

#globals
TOGGLEPLAY = 11
NEXT = 12
LED0 = 15
LED1 = 16
LED2 = 18
LED3 = 36
SAMPLESPATH = "samples"
BLINKSPEED = 0.75
DEBOUNCE = 1

#setup gpio
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TOGGLEPLAY, GPIO.IN)
GPIO.setup(NEXT, GPIO.IN)
GPIO.setup(LED0, GPIO.OUT)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.output(LED0, True)
GPIO.output(LED1, False)
GPIO.output(LED2, False)
GPIO.output(LED3, False)

leds = [LED0, LED1, LED2, LED3]
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
    player = Player(nextfile, False)
    print("ready to play: " + nextfile)

def updateleds():
    global player
    global leds
    global currenttrack
    
    #playing - blink
    if (player.paused == False):
        currentled = leds[currenttrack]
        
        GPIO.output(currentled, False)
        time.sleep(BLINKSPEED)
        GPIO.output(currentled, True)
        time.sleep(BLINKSPEED)
        
    #paused - solid if current track
    else:
        for i in range(0, len(leds)):
            ledon = (i == currenttrack)
            led = leds[i]
            GPIO.output(led, ledon)

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
filenames = listdir(SAMPLESPATH)
setupplayer()

try:
    #runloop
    while True:
        if GPIO.input(TOGGLEPLAY) != playbuttonstate:
            player.toggleplay()
            time.sleep(DEBOUNCE)
            playbuttonstate = GPIO.input(TOGGLEPLAY)
        elif GPIO.input(NEXT) != nextbuttonstate:
            nexttrack()
            time.sleep(DEBOUNCE)
            nextbuttonstate = GPIO.input(NEXT)
        else:
            updateleds()
                
        
except KeyboardInterrupt:
    print("goodbye")
    if (player.paused == False):
        player.toggleplay()
    GPIO.cleanup()
