from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/GuestData', methods=['POST'])
def guest_data():
    data = request.json

    print(data)
    return {"blulpup":"bhgh"}, 200

if __name__ == '__main__':
    app.run(debug=True)