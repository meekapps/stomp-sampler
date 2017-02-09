#implementation for server.py to access file system

from os import listdir
import json

SAMPLESPATH = "samples"

class Samples(object):

    #delete ./samples/<sample>
    #return True if deleted
    @classmethod
    def delete(cls, filename):
        print "deleting sample" + filename
        return True

    #return the list of files in ./samples
    @classmethod
    def get(cls):
        try:
            samples = sorted(listdir(SAMPLESPATH))
            response = {'samples' : samples}
            return json.dumps(response)
            
        # no samples directory yet
        except OSError:
            response = {'samples' : []}
            return json.dumps(response)
    
    #add sample to ./samples/<filename>
    #filename is the next letter in the alphabet with the same file extension
    #returns True if added
    @classmethod
    def add(cls, sample):
        print "adding sample" + sample
        return True



    

    
    