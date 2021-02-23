from flask import Flask, Response, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import datetime

__all__ = ['app']

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

from services import *

@app.route("/test")
def hello():
    return "hello"

if __name__ == "__main__":
    app.secret_key = 'some secret key'
    app.run(host="192.168.0.59", port="5300", debug=True)