import os
from dotenv import load_dotenv
import psycopg


# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém usuário e senha do banco a partir das variáveis de ambiente
user = os.getenv('PG_USER')
pwd = os.getenv('PG_PASS')

# Abre conexão com o banco PostgreSQL usando psycopg
connect = psycopg.connect(
    f'postgresql://{user}:{pwd}@localhost/autentication'
)

# Cria um cursor para executar comandos SQL
cursor = connect.cursor()