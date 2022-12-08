import configparser
from pathlib import Path

__app_name__ = "todo_cli"

import typer

print(Path.home())
print(Path.home().stem)

CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__))
# caminho para o próprio arquivo de configuração.
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.ini"
DEFAULT_DB_FILE_PATH = Path.home().joinpath(f".{Path.home().stem}_todo.json")


print(CONFIG_DIR_PATH)
print(CONFIG_FILE_PATH)
print(DEFAULT_DB_FILE_PATH)

db_path = DEFAULT_DB_FILE_PATH

print(CONFIG_DIR_PATH.mkdir(exist_ok=True))
print(CONFIG_FILE_PATH.touch(exist_ok=True))

config_parser = configparser.ConfigParser()
print(config_parser)

config_parser["General"] = {"database": db_path}
print(config_parser["General"])

with CONFIG_FILE_PATH.open("w") as file:
    config_parser.write(file)
