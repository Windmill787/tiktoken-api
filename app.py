# base
import os

# flask
from flask import Flask, jsonify, request

# tiktoken
import tiktoken

# env
from dotenv import load_dotenv

# load env variables forcefully
load_dotenv(override=True)

app = Flask(__name__)

encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')


@app.route('/', methods=['POST'])
def index():
    if "text" not in request.get_json():
        return jsonify({'message': 'Text is empty'})

    return jsonify({'count': len(encoding.encode(request.get_json()["text"]))})

if __name__ == '__main__':
    app.run(debug=(os.getenv('FLASK_DEBUG') == 'True'), port=os.getenv('FLASK_PORT'), host="0.0.0.0")
