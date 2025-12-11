-- Cria o banco de dados que será usado na aplicação
CREATE DATABASE autentication;


-- Cria a tabela de usuários com campos básicos
CREATE TABLE users (
    id SERIAL PRIMARY KEY,          -- Identificador único autoincrementado
    name TEXT NOT NULL,             -- Nome do usuário
    email TEXT UNIQUE NOT NULL,     -- Email único (não pode repetir)
    password TEXT NOT NULL          -- Senha (armazenada com hash)
);