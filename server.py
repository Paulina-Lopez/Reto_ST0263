from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

### Variables
client = MongoClient('mongodb://localhost:27017/')
db = client['p2p']
peersCollection = db['peers']
filesCollection = db['files']

### ENDPOINTS

### / - Master route
@app.route('/', methods=['GET'])
def master():
    return jsonify({"message": "P2P Project Paulina Lopez"}), 200

### /login - Login route
@app.route('/login', methods=['POST'])
def login ():
    username = request.json['username']
    password = request.json['password']

    previous = getPeerInfo(username)
    if previous:
        if previous['password'] == password:
            return jsonify({"message": "Login successful", "result": True}), 200
        else:
           return jsonify({"message": "Login fail", "result": False}), 500 
    else:
        url = request.json['url']
        peersCollection.insert_one({
            "username": username,
            "password": password,
            "url": url
        })
        return jsonify({"message": "Sign up successful", "result": True}), 200

### /logout - Logout route
@app.route('/logout', methods=['POST'])
def logout():
    username = request.json['username']
    previous = getPeerInfo(username)
    message = ""
    result = False
    if previous:
        message = "The peer " + previous['username'] + " is out"
        result = True
    else:
        message = "The peer " + username + " not found"
    return jsonify({"message": message, "result": result}), 200

### /index - Add files to each peer route
@app.route('/index', methods=['POST'])
def index():
    username = request.json['username']
    files = request.json['files']
    previous = getPeerInfo(username)
    message = ""
    result = []
    
    if previous:
        result = saveFiles(previous, files)
        message = str(len(result)) + " files were added to the peer " + previous['username']
    else:
        message = "The peer " + username + " not found" 
    return jsonify({"message": message, "files": result}), 200

### /search - Search files and location route
@app.route('/search', methods=['POST'])
def search():
    files = request.json['files']
    result = []
    message = ""
    if len(files) > 0:
        result = searchFiles(files)
        message = str(len(result)) + " files of " + str(len(files)) + " requested were found"
    else:
        message = "The files request list is empty or has any problem, please check your information" 
    return jsonify({"message": message, "files": result}), 200


### METHODS

### Get general info of Peers
def getPeerInfo(username):
    previous = peersCollection.find_one({"username": username})
    return previous


### Procedure to save files
def saveFiles (peer, files):
    added = []
    for file in files:
        prevFile = filesCollection.find_one({"filename": file, "peer": peer['username']})
        if not prevFile:
            filesCollection.insert_one({
                "filename": file,
                "peer": peer['username'],
                "url": peer['url']
            })
            added.append(file)
    return added


### Procedure to search files
def searchFiles (files):
    result = []
    for file in files:
        prevFile = filesCollection.find({"filename": file})
        if prevFile:
            for pf in prevFile:
                fl = {
                "filename": pf['filename'],
                "peer": pf['peer'],
                "url": pf['url']
                }
                result.append(fl)
    return result

### MAIN
if __name__ == '__main__':
    app.run(debug=True)
