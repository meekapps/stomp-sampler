#server to update stomp-sampler samples

from flask import Flask
from samples import Samples

app = Flask(__name__)
json_type = 'application/json'

@app.route('/', methods=['GET'])
def index():
    return 'hello'

@app.route('/samples', methods=['GET'])
def get_samples():
    #return list of samples
    return Samples.get()
    
@app.route('/sample/<sample>', methods=['DELETE'])
def delete_sample(sample):
    return Samples.delete(sample)
    
@app.route('/sample', methods=['POST'])
def post_sample():
    sample_data = 'something' #get post data
    return Samples.add(sample_data)
    
def error_response(type, code):
    error = {'error': type}
    failure = Response(response=json.dumps(error),status=code,mimetype=json_type)
    return failure    

if __name__ == '__main__':
	app.run()