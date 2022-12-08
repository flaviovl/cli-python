import time
from typing import Optional

import typer
from rich import print as rprint
from rich.progress import track

app = typer.Typer()

__app_name__ = "todo_cli"
__version__ = "1.01"


def _version_callback(value: bool):
    """Imprimri echo(), levanta um exceção e sair de forma limpa"""

    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "v",
        help="Show the version and exit",
        callback=_version_callback,
        is_eager=True,
    ),
):
    return


if __name__ == "__main__":

    app()
    # typer.run(app())


# @app.command("add")
# def add_task(task: str):
#     with open("tasks.txt", "a") as file:
#         file.write(task + "\n")


# @app.command("list")
# def list_tasks():
#     try:
#         tasks = open("tasks.txt", "r").read()

#         total = 0
#         for _ in track(range(20), description="Processing..."):
#             time.sleep(0.1)
#             total += total + 1
#         rprint(tasks)
#         typer.echo(f"{__app_name__} v{__version__}")
#     except IOError:
# print("Sem tarefas!")
