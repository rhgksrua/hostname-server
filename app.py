from flask import Flask
from socket import gethostname
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '''hostname: {hostname} |
    time: {time}
    '''.format(
        hostname=gethostname(), 
        time=datetime.now().strftime("%H:%M:%S")
    )
