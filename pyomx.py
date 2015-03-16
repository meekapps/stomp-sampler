#omxplayer wrapper

import pexpect
import re

from threading import Thread

class Player(object):
    _LAUNCHOMX = "/usr/bin/omxplayer -o local %s"
    _PAUSE = "p"
    
    paused = False

    def __init__(self, filename, args=None, start_playback=False):
        if not args:
            args = ""            
        command = self._LAUNCHOMX % (filename)
        self._process = pexpect.spawn(command)

    def toggleplay(self) :
        if self._process.send(self._PAUSE):
            self.paused = not self.paused
