import flask
from rich.console import Console 
app = flask.Flask(__name__)
console = Console()

@app.route('/')
def home():
    console.log("ISIS : Service accessed")
    return "Hello, World!"
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    