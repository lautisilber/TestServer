from flask import Flask, request
import json

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

class smart_json:
    def __init__(self, **kwargs):
        self.dict = {}
        for key, value in kwargs.items():
            self.dict[key] = value
    def to_string(self):
        return json.dumps(self.dict)
    def to_dict(self):
        return self.dict

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=HTTP_METHODS)
def main(path):
    path = '/' + path
    if request.method == 'GET':
        j = smart_json(method='GET', path=path, queryparams=request.args)
        print(j.to_dict())
        return j.to_string()
    elif request.method == 'POST':
        print('a', request.data)
        # request data is in bytes
        j = smart_json(method='POST', path=path, data=request.data.decode("utf-8"), form=request.form)
        print(j.to_dict())
        return j.to_string()
    else:
        j = smart_json(method=request.method, path=path)
        print(j.to_dict())
        return j.to_string()

if __name__ == '__main__':
    '''
        To be able to access the server from an external device, host should be 0.0.0.0
    '''
    host = '127.0.0.1' # default is '127.0.0.1'
    port = 5000 # default is 5000
    app.run(debug=True, host=host, port=port)