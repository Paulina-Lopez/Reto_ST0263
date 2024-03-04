from flask import Flask, request, jsonify
import requests
import json
import grpc
import records_pb2
import records_pb2_grpc

app = Flask(__name__)

### LOGIN METHOD
@app.route('/clogin', methods=['POST'])
def login ():
    username = request.json['username']
    password = request.json['password']

    body = {
       "username": username,
       "password": password
    }

    data = request.get_json()
    if 'url' in data:
        body['url'] = data['url']

    result = executeLogin(body)
    return jsonify({"message": result['message']}), 200


### LOGOUT METHOD
@app.route('/clogout', methods=['POST'])
def logout ():
    username = request.json['username']

    body = {
       "username": username,
    }

    result = executeLogout(body)
    return jsonify({"message": result['message']}), 200


### INDEX METHOD
@app.route('/cindex', methods=['POST'])
def index():
    username = request.json['username']
    files = request.json['files']
    stub = []
    body = {
       "username": username,
       "files": files
    }

    result = executeIndex(body)

    if result:
        for f in result['files']:
            stub.append(grpc_client_upload(f))
    return jsonify({"message": result['message'], "files": result['files'], "operation": stub}), 200

### INDEX METHOD
@app.route('/csearch', methods=['POST'])
def search():
    files = request.json['files']
    body = {
        "files": files
    }
    stub = []
    result = executeSearch(body)
    if result:
        for f in result['files']:
            stub.append(grpc_client_download(f['filename']))
    return jsonify({"message": result['message'], "files": result['files'], "operation": stub}), 200

def grpc_client_upload(filename):
    with grpc.insecure_channel('localhost:4999') as channel:
        stub = records_pb2_grpc.FileServiceStub(channel)
        try:
            request = records_pb2.UploadRequest(filename=filename)
            response = stub.Upload(request)
            return response.message
        except grpc.RpcError as e:
            return f"Error during upload: {e.code()} - {e.details()}"
        finally:
            channel.close()

def grpc_client_download(filename):
    with grpc.insecure_channel('localhost:4999') as channel:
        stub = records_pb2_grpc.FileServiceStub(channel)
        try:
            request = records_pb2.DownloadRequest(filename=filename)
            response = stub.Download(request)
            return response.file.content
        except grpc.RpcError as e:
            return f"Error during download: {e.code()} - {e.details()}"
        finally:
            channel.close()
    
def executeLogin (body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://127.0.0.1:5000/login', data=json.dumps(body), headers=headers)
    return response.json()


def executeLogout (body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://127.0.0.1:5000/logout', data=json.dumps(body), headers=headers)
    return response.json()

def executeIndex (body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://127.0.0.1:5000/index', data=json.dumps(body), headers=headers)
    return response.json()

def executeSearch (body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://127.0.0.1:5000/search', data=json.dumps(body), headers=headers)
    return response.json()

### MAIN
if __name__ == '__main__':
    app.run(debug=True, port=5001)
