import typer

app = typer.Typer()


@app.callback()
def callback():
    pass


@app.command()
def execute(option: str = typer.Option()):
    print('hello world')


if __name__ == '__main__':
    app()
