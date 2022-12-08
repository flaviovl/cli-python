# CLI de tarefas pendentes com Python e Typer



# Visão geral do projeto

Aplicativo de linha comando (CLI) amigavel, que permita que seus usuários
interajam com o aplicativo e gerenciem suas listas de tarefas. 


* Usado o padrão de arquitetura MVC (separação de preocupações)
* Typer para construir a CLI do aplicativo de tarefas
* Módulo do Python json para gerenciar armazenamento.
* pytest como uma ferramenta para testar o aplicativo CLI.

* Usar arquivo JSON para armazenar os JSON é um banco de intercâmbio formato que é humano, legível e gravável. 


Principais comandos
Comando	                Descrição
init	                Inicializa o banco de
add DESCRIPTION      	Adiciona uma nova tarefa ao banco de
list                	Lista todas as tarefas no banco de
complete TODO_ID	    Conclui uma tarefa definindo-a como concluída usando seu ID
remove TODO_ID          Remove uma tarefa do banco de
clear	                Remove todas as tarefas ao limpar o banco de

Testar um aplicativo Typer é direto porque a biblioteca se integra muito bem com o pytest


Definir configuraçoes do aplicativo:
Como o aplicativo se conecta e abre um arquivo?
    . Fornecer o caminho do arquivo dinamicamente (variavel de ambiente para armazenar caminho do arquivo)
    . Criar um arquivo de configuração no qual armazena o caminho do arquivo.

    
