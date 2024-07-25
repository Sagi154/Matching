from flask import Flask, request, jsonify
from flask_cors import CORS
from main import *
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/GuestData', methods=['POST'])
def guest_data():
    guest_data = request.json
    available_hosts = new_guest(guest_data)
    print(available_hosts)
    return jsonify(available_hosts), 200


@app.route('/HostData', methods=['POST'])
def host_data():
    host_data = request.json
    new_host(host_data)
    return {"Adding Host: " : "success" }, 200


if __name__ == '__main__':
    app.run(debug=True)