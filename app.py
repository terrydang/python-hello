from flask import Flask, request, jsonify
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello world!"


if __name__ == '__main__':
    app.run(port=8080, host="0.0.0.0")
