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


@app.route('/', methods=['POST'])
def index():
    # get text from form
    form = request.get_json()

    if "text" not in form:
        return jsonify({'message': 'Text is empty'})

    text = form["text"]

    encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')

    num_tokens = len(encoding.encode(text))

    return jsonify({'count': num_tokens})

if __name__ == '__main__':
    app.run(debug=(os.getenv('FLASK_DEBUG') == 'True'), port=os.getenv('FLASK_PORT'), host="0.0.0.0")
