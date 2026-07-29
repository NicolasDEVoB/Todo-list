# Todo List API

Este projeto é uma API em FastAPI para um gerenciador de tarefas (todo list) em fase inicial de desenvolvimento.

## Requisitos

- Python 3.10 ou superior
- pip

## Como rodar o projeto

1. Entre na pasta do projeto:

   ```bash
   cd /home/nicolas/Projects/Todo-list
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicie a aplicação:

   ```bash
   uvicorn app.main:app --reload
   ```

5. Acesse a API no navegador:

   - Endpoint inicial: http://127.0.0.1:8000/
   - Documentação automática: http://127.0.0.1:8000/docs

## Estado atual

Nesta fase, a aplicação já está respondendo no endpoint raiz com um JSON simples:

```json
{
  "message": "OK"
}
```

Para encerrar o servidor, pressione Ctrl+C no terminal.
