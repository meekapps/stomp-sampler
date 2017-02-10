#implementation for server.py to access file system

import os
from os import listdir
from werkzeug import secure_filename

ALLOWEDTYPES = set(['mp3', 'wav'])
SAMPLESPATH = "samples"

class Samples(object):

    #delete ./samples/<sample>
    #return True if deleted
    @staticmethod
    def delete(filename):
        path = SAMPLESPATH + '/' + filename
        try:
            os.remove(path)
            return response(True)
            
        # file does not exist
        except OSError:
            return response(False)

    #return the list of files in ./samples
    @staticmethod
    def get():
        try:
            samples = sorted(listdir(SAMPLESPATH))
            samples = [s for s in samples if allowed(s)]
            return samples
            
        # no samples directory yet
        except OSError:
            return None
    
    #add sample to ./samples/<filename>
    #filename is the next letter in the alphabet with the same file extension
    #returns True if added
    @staticmethod
    def add(file):
        if file == None:
            response(False)
            
        #remove unsupported chars
        filename = secure_filename(file.filename)    
        
        #check file types
        if allowed(filename) == False:
            return response(False)
        
        try:
            file.save(os.path.join(SAMPLESPATH, filename))
            return response(True)
            
        except OSError:
            return response(False)
                 
def allowed(filename):
    return  '.' in filename and filename.rsplit('.', 1)[1] in ALLOWEDTYPES
    
        
    