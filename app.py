from flask import flask
from socket import gethostname
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World! ' + gethostname()