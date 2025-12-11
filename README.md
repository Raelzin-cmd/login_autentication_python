# 🛡️ API de Autenticação – Flask + PostgreSQL + JWT

Este projeto é uma API simples de autenticação construída com Flask, PostgreSQL, JWT, bcrypt e Docker.
Permite registrar usuários, realizar login com geração de token JWT e acessar rotas protegidas.

---

## 🚀 Tecnologias Utilizadas

* Python 3
* Flask
* PostgreSQL
* psycopg
* bcrypt
* JWT (PyJWT)
* python-dotenv
* Docker + Docker Compose

---

## 📁 Estrutura do Projeto

```
project/
│── .venv/                     # Ambiente virtual Python
│── controllers/
│   ├── login.py               # Controller de login
│   ├── users.py               # Controller de registro e rota /user
│── data/
│   └── postgres/              # Volume local do PostgreSQL (Docker)
│── database/
│   ├── connection.py          # Conexão com o banco
│   ├── dump.sql               # Script para criação do banco/tabela
│   └── users_repository.py    # CRUD de usuários
│── middlewares/
│   └── middleware.py          # Middleware de autenticação
│── app.py                     # Arquivo principal da aplicação Flask
│── docker-compose.yml         # Subida do PostgreSQL
│── requirements.txt           # Dependências do Python
│── .env                       # Variáveis de ambiente (local)
└── README.md
```

---

## ⚙️ Configuração do Ambiente

### 1️⃣ Criar e ativar ambiente virtual (.venv)

```
python -m venv .venv
```

Ativar:

* Windows

```
.venv\Scripts\activate
```

* Linux/Mac

```
source .venv/bin/activate
```

---

### 🔧 Instalar dependências

```
pip install -r requirements.txt
```

---

### 📝 Configuração do arquivo .env

Crie um arquivo .env na raiz:

```
PG_USER=seu_usuario
PG_PASS=sua_senha
CONTAINER_NAME=postgres-auth
PORT=5432
```

---

### 🐘 Subir o PostgreSQL com Docker

```
docker-compose up -d
```

Isso cria o container e gera os dados em:

```
/data/postgres
```

---

### 🗄️ Criar banco e tabela

Execute o conteúdo de `database/dump.sql`:

```SQL
CREATE DATABASE autentication;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
```

---

### ▶️ Rodar o servidor Flask

Com o ambiente ativo:

```
python app.py
```

Servidor iniciará em:

```
http://localhost:3000
```

---

## 🔑 Rotas da API
### 📌 POST /register

Registra um novo usuário.

**Body JSON:**

```json
{
  "name": "John Doe",
  "email": "john@mail.com",
  "password": "123456"
}
```

**Retorno (201):**

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@mail.com",
  "password": "<hashed>"
}
```

---

### 📌 POST /login

Gera token JWT válido por 8h.

**Body JSON:**

```json
{
  "email": "john@mail.com",
  "password": "123456"
}
```

**Retorno (200):**

```json
{
  "user": { ... },
  "token": "jwt.token.aqui"
}
```

---

### 📌 GET /user (rota protegida)

Header necessário:

```
Authorization: Bearer <seu_token>
```

**Retorno (200):**

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@mail.com",
  "password": "<hashed>"
}
```

---

### 🧩 Middleware de Autenticação

O arquivo `middlewares/middleware.py` intercepta todas as rotas, exceto:

* `/login`
* `/register`

Ele valida:

* Se o token existe
* Se está no formato Bearer
* Se não expirou
* Se o usuário existe no banco

Após isso, insere:

```bash
request.user
```

Para ser utilizado nos controllers.

---

### 🛠️ Scripts SQL

O arquivo `database/dump.sql` contém toda a estrutura necessária do banco.

---

### 📦 requirements.txt oficial

```txt
psycopg[binary]
flask
bcrypt
pyjwt
python-dotenv
```

---

### 📌 GitIgnore recomendado

```
venv/
__pycache__/
*.pyc
.env
data/postgres/
.vscode/
```

---

### 🎯 Conclusão

Este projeto fornece uma estrutura limpa e simples para:

✔ Registro de usuários <br>
✔ Login <br>
✔ Geração de JWT <br>
✔ Rota protegida com Middleware <br>
✔ Banco PostgreSQL via Docker <br>
✔ Organização por controllers, middlewares e repositórios