# Escopo do Projeto: API de To-Do List

**Objetivo:** praticar o fluxo completo de desenvolvimento e deploy, do ambiente local até produção com banco relacional e Docker.

**Stack sugerida:** Python + FastAPI + SQLAlchemy + SQLite (local) → PostgreSQL (produção) + Docker + Render/Railway

---

## Fase 0 — Setup do projeto

**Objetivo:** preparar o ambiente antes de escrever qualquer lógica de negócio.

- [x] Criar pasta do projeto
- [x] Criar e ativar ambiente virtual (`venv`)
- [x] Inicializar `git init`
- [x] Criar `.gitignore` (venv/, __pycache__/, .env, *.db, .DS_Store)
- [x] Criar repositório no GitHub e conectar
- [x] Instalar FastAPI, uvicorn, SQLAlchemy
- [x] Criar `requirements.txt` inicial
- [x] Estrutura de pastas inicial:

```
todo-app/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── crud.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

**Entregável:** projeto rodando localmente com uma rota `GET /` respondendo "ok".

---

## Fase 1 — Modelagem de dados

**Objetivo:** definir a estrutura da tabela `tasks` antes de criar as rotas.

- [ ] Definir os campos da tarefa:
  - `id` (int, chave primária)
  - `title` (string, obrigatório)
  - `description` (string, opcional)
  - `completed` (boolean, default False)
  - `created_at` (datetime, automático)
- [ ] Criar o model no SQLAlchemy (`models.py`)
- [ ] Criar os schemas Pydantic para entrada/saída de dados (`schemas.py`)
- [ ] Configurar conexão com SQLite em `database.py`
- [ ] Testar criação automática da tabela ao rodar o app

**Entregável:** arquivo `todo.db` (SQLite) criado localmente com a tabela `tasks`.

---

## Fase 2 — CRUD local (SQLite)

**Objetivo:** implementar as operações básicas e testar tudo localmente.

Rotas a criar:

| Método | Rota | Ação |
|---|---|---|
| POST | `/tasks` | Criar tarefa |
| GET | `/tasks` | Listar todas as tarefas |
| GET | `/tasks/{id}` | Buscar uma tarefa |
| PUT | `/tasks/{id}` | Atualizar tarefa |
| DELETE | `/tasks/{id}` | Deletar tarefa |
| PATCH | `/tasks/{id}/complete` | Marcar como concluída |

- [ ] Implementar cada rota, uma por vez
- [ ] Testar cada rota com Postman/Insomnia/curl antes de seguir pra próxima
- [ ] Adicionar tratamento de erro (ex: tarefa não encontrada → 404)
- [ ] Adicionar validação de dados (ex: `title` não pode ser vazio)
- [ ] Testar documentação automática do FastAPI em `/docs`

**Entregável:** CRUD completo funcionando localmente, testável via `/docs`.

---

## Fase 3 — Variáveis de ambiente

**Objetivo:** preparar o projeto para não depender de valores fixos no código.

- [ ] Instalar `python-dotenv`
- [ ] Criar `.env` local com `DATABASE_URL=sqlite:///./todo.db`
- [ ] Ler `DATABASE_URL` do ambiente em `database.py` em vez de fixo no código
- [ ] Criar `.env.example` (sem valores sensíveis) para referência no repositório
- [ ] Confirmar que `.env` está no `.gitignore`

**Entregável:** app não quebra se `.env` mudar de SQLite para outro banco — só muda a variável.

---

## Fase 4 — Dockerização

**Objetivo:** empacotar o app pra rodar igual em qualquer ambiente.

- [ ] Criar `Dockerfile`:
  - Imagem base Python
  - Copiar `requirements.txt` e instalar dependências
  - Copiar o código
  - Expor porta (ex: 8000)
  - Comando de start com `uvicorn`
- [ ] Criar `.dockerignore` (venv/, __pycache__/, .git/, .env)
- [ ] Buildar a imagem localmente: `docker build -t todo-app .`
- [ ] Rodar o container localmente: `docker run -p 8000:8000 todo-app`
- [ ] Testar que a API responde normalmente rodando dentro do container

**Entregável:** app rodando via Docker localmente, idêntico ao ambiente que vai pra produção.

---

## Fase 5 — Banco de produção (PostgreSQL)

**Objetivo:** trocar SQLite por um banco que aguenta produção de verdade.

- [ ] Criar instância PostgreSQL (a própria Render/Railway oferece isso gratuitamente)
- [ ] Instalar driver `psycopg2-binary` (ou `asyncpg` se for async)
- [ ] Adicionar `docker-compose.yml` para rodar app + Postgres juntos localmente:

```
services:
  app:
    build: .
    ports: ["8000:8000"]
    depends_on: [db]
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: tododb
      POSTGRES_PASSWORD: postgres
```

- [ ] Testar localmente com `docker-compose up`, apontando `DATABASE_URL` pro Postgres do compose
- [ ] Confirmar que os models do SQLAlchemy funcionam igual com Postgres (mudança só na connection string)

**Entregável:** app + banco Postgres rodando juntos localmente via Docker Compose.

---

## Fase 6 — Deploy em produção

**Objetivo:** subir o projeto de verdade.

- [ ] Escolher plataforma (Render é o mais direto pra esse fluxo)
- [ ] Criar o serviço Web apontando pro repositório GitHub
- [ ] Criar o banco Postgres gerenciado na própria plataforma
- [ ] Configurar variável de ambiente `DATABASE_URL` no painel, apontando pro Postgres de produção
- [ ] Configurar a plataforma para usar o `Dockerfile` do projeto (deploy via Docker)
- [ ] Fazer o primeiro deploy
- [ ] Testar as rotas em produção via `/docs` (URL pública)

**Entregável:** API pública rodando, com banco Postgres real, deployada via Docker.

---

## Fase 7 — Pós-deploy

**Objetivo:** deixar o projeto em estado profissional e testar o ciclo de iteração.

- [ ] Configurar CORS (caso pretenda consumir a API de um front-end depois)
- [ ] Adicionar logs básicos (prints estruturados ou logging do Python)
- [ ] Escrever `README.md` com instruções de setup, rotas disponíveis e como rodar local/Docker
- [ ] Fazer uma alteração pequena localmente (ex: novo campo `priority` na tarefa), commitar, dar push e confirmar que o deploy automático atualiza a produção sem quebrar os dados existentes

**Entregável:** projeto documentado, com ciclo `código → commit → push → deploy` validado na prática.

---

## Fase 8 (opcional, extensão futura) — Autenticação

Só depois que o fluxo acima estiver 100% consolidado:

- [ ] Tabela `users`
- [ ] Login com JWT
- [ ] Campo `user_id` em `tasks`
- [ ] Middleware de autenticação nas rotas

Essa fase ensina migração de schema em produção sem perder dados — vale fazer como um segundo ciclo depois que o básico estiver redondo.

---

## Resumo do progresso técnico por fase

| Fase | O que muda tecnicamente |
|---|---|
| 0-2 | Python puro, SQLite, sem Docker |
| 3 | Introdução de variáveis de ambiente |
| 4 | Introdução de Docker (ainda com SQLite) |
| 5 | Troca de banco (SQLite → Postgres) + Docker Compose |
| 6 | Deploy real em nuvem |
| 7 | Boas práticas de produção |
| 8 | Autenticação (opcional) |

Cada fase é um commit (ou vários) — assim você tem um histórico claro de evolução do projeto no GitHub.
