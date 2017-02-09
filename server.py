#server to update stomp-sampler samples

from flask import Flask, request
from samples import Samples

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'hello'

#curl -X GET http://127.0.0.1:5000/samples
@app.route('/samples', methods=['GET'])
def get_samples():
    #return list of samples
    return Samples.get()
    
#curl -X DELETE http://127.0.0.1:5000/sample/a.wav
@app.route('/sample/<sample>', methods=['DELETE'])
def delete_sample(sample):
    return Samples.delete(sample)
    
#curl -X POST -F file=@testfile http://127.0.0.1:5000/sample
@app.route('/sample', methods=['POST'])
def post_sample():
    file = request.files['file']
    return Samples.add(file)

if __name__ == '__main__':
	app.run()