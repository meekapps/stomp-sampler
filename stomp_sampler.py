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
        print("fnameatindex: " + fname)
        return fname

    #setup gpio
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TOGGLEPLAY, GPIO.IN)
    GPIO.setup(LED0, GPIO.OUT)
    led0state = False
    GPIO.output(LED0, led0state)
    buttonstate = GPIO.input(TOGGLEPLAY)
    print("waiting for input...")

    #read samples
    filenames = listdir(SAMPLESPATH)

    #setup omxplayer
    player = Player(filenameatindex(0))
    player.toggleplay()
    while True:
        if GPIO.input(TOGGLEPLAY) != buttonstate:
            print("play/pause")
            player.toggleplay()
            GPIO.output(LED0, True)
            time.sleep(1.5)
            buttonstate = GPIO.input(TOGGLEPLAY)
        
except KeyboardInterrupt:
    print("goodbye")
    GPIO.cleanup()
