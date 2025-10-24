import flask
from rich.console import Console 

app = flask.Flask(__name__)
console = Console()

@app.route('/')
def home():
    console.log("[bold green]ISIS : Service accessed[/bold green]")
    return "Hello, World!"

@app.route('/calculate?eq=<equation>')
def calculate(equation):
    try:
        result = eval(equation)
        console.log(f"[bold blue]ISIS : Calculation performed: {equation} = {result}[/bold blue]")
        return str(result)  
    except Exception as e:
        console.log(f"[bold red]ISIS Error in calculation: {e}[/bold red]")
        return "Error in calculation", 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    