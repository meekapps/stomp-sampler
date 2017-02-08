#python omxplayer wrapper

import subprocess

class Player(object):
    #omxplayer
    OMX = "/usr/bin/omxplayer"
    OUTPUT = "alsa" #alsa for pHAT DAC (pi zero), local for bult-in audio (pi a+)
    TOGGLEPLAY = "p"
    STOP = "q"
    
    paused = False

    def setupPlayer(self):
        self.process = subprocess.Popen([self.OMX, '-o', self.OUTPUT, self.currentFilename], stdin=subprocess.PIPE)
  
    def __init__(self, filename):
        print(filename)
        self.currentFilename = filename        
        self.setupPlayer()        
        self.toggleplay()

    def toggleplay(self):
        #Finished playing, restart current sample
        if self.pollDone() == True:
            self.setupPlayer()
        else:
            self.process.stdin.write(self.TOGGLEPLAY)
        
        self.paused = not self.paused
        
        if self.paused:
            print("toggleplay - paused")
        else:
            print("toggleplay - playing")

    def stop(self):
        print("stop")
        self.paused = True
        
        if self.process.poll() != 0:
            self.process.stdin.write(self.STOP)
            self.process.terminate()

    def pollDone(self):
       code = self.process.poll()
       if code == 0:
          self.paused = True
          return True
       else:
          return False


            
