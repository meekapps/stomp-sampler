#implementation for server.py to access file system

import os
from os import listdir
from werkzeug import secure_filename

ALLOWEDTYPES = set(['mp3'])
MAXSAMPLES=5
SAMPLESPATH = "samples"

class Samples(object):

    #add sample to ./samples/<filename>
    #filename is the next letter in the alphabet with the same file extension
    #returns True if added
    @staticmethod
    def add(file):
        if file == None:
            False
            
        #remove unsupported chars
        filename = secure_filename(file.filename)    
        
        #check file types
        if allowed(filename) == False:
            return False
        
        try:
            file.save(os.path.join(SAMPLESPATH, filename))
            return True
            
        except OSError:
            return False
            
    @staticmethod
    def has_max():
        samples = Samples.get_all()
        return True if len(samples) >= MAXSAMPLES else False

    #delete ./samples/<sample>
    #return True if deleted
    @staticmethod
    def delete(filename):
        path = SAMPLESPATH + '/' + filename
        try:
            os.remove(path)
            return True
            
        # file does not exist
        except OSError:
            return False
        
    #return the list of files in ./samples
    @staticmethod
    def get_all():
        try:
            samples = sorted(listdir(SAMPLESPATH))
            samples = [s for s in samples if allowed(s)]
            return samples
            
        # no samples directory yet
        except OSError:
            return None
                 
def allowed(filename):
    return  '.' in filename and filename.rsplit('.', 1)[1] in ALLOWEDTYPES
    
        
    