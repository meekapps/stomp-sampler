#stomp_sampler

try:
    import RPi.GPIO as GPIO
    import time
    from os import listdir
    from os.path import isfile, join
    from pyomx import Player

    #globals
    TOGGLEPLAY = 11
    NEXT = 12
    LED0 = 15
    SAMPLESPATH = "samples"
    BLINKSPEED = 0.75
    DEBOUNCE = 1.5

    def filenameatindex(index):
        fname = SAMPLESPATH + "/" + filenames[index]
        return fname

    def updateled(led):
        #playing - blink
        if (player.paused == False):
            GPIO.output(led, False)
            time.sleep(BLINKSPEED)
            GPIO.output(led, True)
            time.sleep(BLINKSPEED)
        #paused - solid
        else:
            GPIO.output(LED0, True)

    def nexttrack():
        player.stop()
        global currenttrack
        
        if (currenttrack + 1 < len(filenames)):
            currenttrack += 1
        else:
            currenttrack = 0
        nextfile = filenameatindex(currenttrack)
        print("up next: " + nextfile)

    #setup gpio
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TOGGLEPLAY, GPIO.IN)
    GPIO.setup(NEXT, GPIO.IN)
    GPIO.setup(LED0, GPIO.OUT)
    GPIO.output(LED0, True)
    playbuttonstate = GPIO.input(TOGGLEPLAY)
    print("waiting for input...")

    #read samples
    currenttrack = 0
    filenames = listdir(SAMPLESPATH)

    #setup omxplayer with first sample, don't autoplay
    player = Player(filenameatindex(currenttrack), False)

    #runloop
    while True:
        if GPIO.input(TOGGLEPLAY) != playbuttonstate:
            player.toggleplay()
            time.sleep(DEBOUNCE)
            playbuttonstate = GPIO.input(TOGGLEPLAY)
        elif GPIO.input(NEXT):
            nexttrack()
            time.sleep(DEBOUNCE)            
        else:
            updateled(LED0)
                
        
except KeyboardInterrupt:
    print("goodbye")
    if (player.paused == False):
        player.toggleplay()
    GPIO.cleanup()
