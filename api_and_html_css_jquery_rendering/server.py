import json
from flask import Flask, send_from_directory, jsonify, request

app = Flask(__name__)
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

@app.route('/')
def index():
    return send_from_directory('.', 'ui/index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('ui', filename)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, use_reloader=True, threaded=True)
