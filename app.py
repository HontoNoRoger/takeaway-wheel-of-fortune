from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def wheel_of_fortune():
    with open('config/config.yaml', 'r') as f:
        config = load(f, Loader=Loader)

    return render_template('index.html', meals=config['meals'])
