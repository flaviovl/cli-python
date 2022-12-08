# CLI de tarefas pendentes com Python e Typer



## Visão geral do projeto

    Aplicativo de linha comando (CLI) amigavel, que permita que seus usuários
    interajam com o aplicativo e gerenciem suas listas de tarefas. 


* Typer para construir a CLI do aplicativo de tarefas
* Módulo do Python json para gerenciar armazenamento.
* pytest como uma ferramenta para testar o aplicativo CLI.
* Usar arquivo JSON para armazenar os JSON é um banco de intercâmbio formato que é humano, legível e gravável. 



| Comando            | Descrição                                                  |
| ------------------ | ------------------------------------------------------------ |
| `init`             | Inicializa o banco de dados.                                 |
| `add DESCRIPTION`  | Adiciona uma nova tarefa ao bds com uma `descrição`.         |
| `list`             | Lista todas as tarefas.                                      |
| `complete TODO_ID` | Conclui uma tarefa definindo como concluída                  |
| `remove TODO_ID`   | Remover uma tarefa                                           |
| `clear`            | Remover todas as tarefas ao limpar o banco de dados.         |



Obs: Testar um aplicativo Typer é direto porque a biblioteca se integra muito bem com o pytest


* Definir configuraçoes do aplicativo:
    > Como o aplicativo se conecta e abre um arquivo?
    > Fornecer o caminho do arquivo dinamicamente (variavel de ambiente para armazenar caminho do arquivo)  
    > Criar um arquivo de configuração no qual armazena o caminho do arquivo.  

    
