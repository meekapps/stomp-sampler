#python omxplayer wrapper

import pexpect
import re

from threading import Thread

class Player(object):
    #omxplayer
    LAUNCHOMX = "/usr/bin/omxplayer -o local %s"
    PAUSE = "p"
    NEXT = "k"
    STOP = "q"
    
    #omxplayer pexpect regexes
    _STATUS_REXP = re.compile(r"V :\s*([\d.]+).*")
    _DONE_REXP = re.compile(r"have a nice day.*")
    
    paused = False

    def __init__(self, filename, args=None, start_playback=False):
        if not args:
            args = ""            
        command = self.LAUNCHOMX % (filename)
        self.process = pexpect.spawn(command)
        
        self.done_poll_thread = Thread(target = self.polldone)
        self.done_poll_thread.start()
        
        if (start_playback == False):
            self.toggleplay()

    def toggleplay(self):
        if self.process.send(self.PAUSE):
            self.paused = not self.paused
            if (self.paused):
                print("pause")
            else:
                print("play")

    def stop(self):
        print("stop")
        self.paused = True
        self.process.send(self.STOP)
        self.process.terminate(force=True)

    def polldone(self):
        shouldpoll = True
        while shouldpoll:
            index = self.process.expect([self._STATUS_REXP,
                                        pexpect.TIMEOUT,
                                        pexpect.EOF,
                                        self._DONE_REXP])
            if index == 3:
                print("done")
                shouldpoll = False
                #todo: printing done at right time, paused is not signaling leds
                #to stop blinking correctly. might be a threading issue.
                #also can't quit while playing
                paused = True


            
