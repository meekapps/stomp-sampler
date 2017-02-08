#server to update stomp-sampler samples

from flask import Flask
from samples import Samples

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'hello'

@app.route('/samples', methods=['GET'])
def get_samples():
    #return list of samples
    return Samples.get()
    
@app.route('/sample/<sample>', methods=['DELETE'])
def delete_sample(sample):
    deleted = Samples.delete(sample)
    return "deleted"
    
@app.route('/sample', methods=['POST'])
def post_sample():
    sample_data = 'something'
    added = Samples.add(sample_data)
    return "added"
    
if __name__ == '__main__':
	app.run()