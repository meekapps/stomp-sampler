#implementation for server.py to access file system

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
        print "getting samples..."
        return "samples..."
    
    #add sample to ./samples/<filename>
    #filename is the next letter in the alphabet with the same file extension
    #returns True if added
    @classmethod
    def add(cls, sample):
        print "adding sample" + sample
        return True


    

    
    