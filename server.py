import flask
from rich.console import Console 
app = flask.Flask(__name__)
console = Console()

@app.route('/')
def home():
    console.log("ISIS : Service accessed")
    return "Hello, World!"
