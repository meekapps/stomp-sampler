#server to update stomp-sampler samples

from flask import Flask, render_template, Response, request, send_from_directory
from gevent.wsgi import WSGIServer
import json
from samples import Samples

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    samples = Samples.get_all()
    return render_template('index.html', samples=samples)

@app.route('/sample/<sample>', methods=['GET'])
def get_sample(sample):
    return send_from_directory(Samples.get_samples_path(), sample)

#curl -X GET http://127.0.0.1:5000/samples
@app.route('/samples', methods=['GET'])
def get_samples():
    #return list of samples
    samples =  Samples.get_all()
    response = {'samples' : samples}
    return json.dumps(response)
    
#curl -X DELETE http://127.0.0.1:5000/sample/a.wav
@app.route('/sample/<sample>', methods=['DELETE'])
def delete_sample(sample):
    deleted = Samples.delete(sample)
    return response(deleted)
    
#curl -X POST -F file=@testfile http://127.0.0.1:5000/sample
@app.route('/sample', methods=['POST'])
def post_sample():
    file = request.files['file']
    added = Samples.add(file)
    return response(added)

#returns success/failure response json
def response(success):
    response = {'success' : success}
    return json.dumps(response) 

if __name__ == '__main__':
	#app.run(port=5000)
    server = WSGIServer(('', 5000), app)
    server.serve_forever()
    