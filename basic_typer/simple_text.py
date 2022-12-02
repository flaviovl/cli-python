import typer

app = typer.Typer()


@app.command('name')
def print_text(first_name: str, last_name: str = ' '):
    print(f"Ola meu nome é {first_name}", end=" ")
    if last_name:
        print(last_name)


if __name__ == "__main__":
    app()
