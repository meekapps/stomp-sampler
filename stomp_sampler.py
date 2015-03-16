#stomp_sampler

try:
    import RPi.GPIO as GPIO
    import time
    from os import listdir
    from os.path import isfile, join
    from pyomx import Player

    #globals
    TOGGLEPLAY = 11
    LED0 = 15
    SAMPLESPATH = "samples"

    def filenameatindex(index):
        fname = SAMPLESPATH + "/" + filenames[index]
        return fname

    def updateled(led):
        #playing - blink
        if (player.paused == False):
            GPIO.output(led, False)
            time.sleep(1)
            GPIO.output(led, True)
            time.sleep(1)
        #paused - solid
        else:
            GPIO.output(LED0, True)

    #setup gpio
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TOGGLEPLAY, GPIO.IN)
    GPIO.setup(LED0, GPIO.OUT)
    GPIO.output(LED0, True)
    buttonstate = GPIO.input(TOGGLEPLAY)
    print("waiting for input...")

    #read samples
    filenames = listdir(SAMPLESPATH)

    #setup omxplayer
    player = Player(filenameatindex(0), False)

    #runloop
    while True:
        if GPIO.input(TOGGLEPLAY) != buttonstate:
            player.toggleplay()
            #debounce
            time.sleep(1.5)
            buttonstate = GPIO.input(TOGGLEPLAY)
        else:
            updateled(LED0)
                
        
except KeyboardInterrupt:
    print("goodbye")
    GPIO.cleanup()
