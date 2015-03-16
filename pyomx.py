#omxplayer wrapper

import pexpect
import re

from threading import Thread

class Player(object):
    LAUNCHOMX = "/usr/bin/omxplayer -o local %s"
    PAUSE = "p"
    
    paused = False

    def __init__(self, filename, args=None, start_playback=False):
        if not args:
            args = ""            
        command = self.LAUNCHOMX % (filename)
        self._process = pexpect.spawn(command)
        if (start_playback == False):
            self.toggleplay()

    def toggleplay(self) :
        if self._process.send(self.PAUSE):
            self.paused = not self.paused
            if (self.paused):
                print("pause")
            else:
                print("play")
