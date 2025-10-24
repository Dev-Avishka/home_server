import flask
from rich.console import Console 

app = flask.Flask(__name__)
console = Console()

@app.route('/')
def home():
    console.log("[bold green]ISIS : Service accessed[/bold green]")
    return "Hello, World!"

@app.route('/sendimage')
def serve_image():
    return flask.send_file('images/image.jpg', mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    