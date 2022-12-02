import time
from pathlib import Path

import typer
from rich import inspect, pretty
from rich import print as rprint
from rich.progress import track

app = typer.Typer()

@app.command("add")
def add_task(task: str):
    with open('tasks.txt', 'a') as file:
        file.write(task+'\n')
        

@app.command("list")
def list_tasks():
    try:
        tasks = open('tasks.txt', 'r').read()
       
       
        total = 0
        for _ in track(range(20), description="Processing..."):
            time.sleep(0.1)
            total += total +1
        rprint(tasks)
    except IOError:
        print("Sem tarefas!")
    

# @app.command()
# def rm_task():
    

if __name__ == "__main__":
    app()
    # typer.run(app())

