# pip install "typer[all]"
# pip install rich

import typer
from fake_db import fake_db
from rich import print as rprint


def main():
    rprint("[bold red]Alera![/bold red] [green]Ruby é [/green] dominadora! :boom:")

    rprint(fake_db)


if __name__ == "__main__":
    typer.run(main)
