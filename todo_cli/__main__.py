import os
import sys

import cli
from rich import print

__app_name__ = "todo_cli"

print("=^" * 60)

# Retorna o caminho absoluto para o diretório
# fpath = os.path.join(os.path.dirname(__file__), 'utils')
# sys.path.append(fpath)
print(sys.path)

print("=^" * 60)


def main():
    print(__app_name__)
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()
