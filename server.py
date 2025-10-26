from logs import log
import flask
from db import *
from routes import bp as routes_bp
import os
from flask import send_from_directory



app = flask.Flask(__name__)


app.register_blueprint(routes_bp)

PUBLIC_DIR = os.path.join(os.path.dirname(__file__), 'public')

@app.route('/')
def serve_index():
    return send_from_directory(PUBLIC_DIR, 'index.html')

@app.route('/<path:path>')
def serve_public(path):
    return send_from_directory(PUBLIC_DIR, path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    