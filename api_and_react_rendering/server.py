import os
import json
from flask import Flask, send_from_directory, jsonify, request, Response

app = Flask(__name__, static_folder='react_app/build')
from flask_cors import CORS
CORS(app)

@app.route('/my_get_api')
def getapi():
    response = jsonify({"response":"This is a dummy response"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/my_post_api', methods=['POST'])
def get_projects(request=request):
    req_data = request.get_json()
    print(req_data)
    response = jsonify({"your req data was":req_data})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, use_reloader=True, threaded=True)
