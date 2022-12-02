import typer

app = typer.Typer()


@app.command("add")
def add_task(task: str):
    with open('tasks.txt', 'a') as file:
        file.write(task+'\n')

        

@app.command("list")
def list_tasks():
    try:
        tasks = open('tasks.txt').read()
        print(tasks)
    except IOError:
        print("Sem tarefas!")
    


if __name__ == "__main__":
    app()
