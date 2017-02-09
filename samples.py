#implementation for server.py to access file system

import os
from os import listdir
import json
from werkzeug import secure_filename

ALLOWEDTYPES = set(['wav', 'mp3'])
SAMPLESPATH = "samples"

class Samples(object):

    #delete ./samples/<sample>
    #return True if deleted
    @staticmethod
    def delete(cls, filename):
        path = SAMPLESPATH + '/' + filename
        try:
            os.remove(path)
            return response(True)
            
        # file does not exist
        except OSError:
            return response(False)

    #return the list of files in ./samples
    @staticmethod
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
        
def response(success):
    response = {'success' : success}
    return json.dumps(response)
    
        
    