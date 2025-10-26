from rich.console import Console 

logs_txt = "logs.txt"
console = Console()
def log(log_message,color):
    console_log_message = f"[bold {color}]{log_message}[/bold {color}]"
    console.log(console_log_message)
    with open(logs_txt, "a") as log_file:
        log_file.write(log_message + "\n")
        log_file.flush()