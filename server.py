#server to update stomp-sampler samples

from flask import Flask, redirect, render_template, Response, request, send_from_directory
import json
from samples import Samples

app = Flask(__name__, static_folder = 'samples')

@app.route('/', methods=['GET'])
def index():
    samples = Samples.get_all()
    return render_template('index.html', samples=samples, static_dir=static_dir)

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
    Samples.delete(sample)
    
    samples =  Samples.get_all()
    response = {'samples' : samples}
    return json.dumps(response)
    
#curl -X POST -F file=@testfile http://127.0.0.1:5000/sample
@app.route('/sample', methods=['POST'])
def post_sample():
    file = request.files['file']
    added = Samples.add(file)
    return redirect("/")

#returns success/failure response json
def response(success):
    response = {'success' : success}
    return json.dumps(response) 

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)
	    