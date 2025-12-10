import os
from dotenv import load_dotenv
import psycopg

load_dotenv()

user = os.getenv('PG_USER')
pwd = os.getenv('PG_PASS')

connect = psycopg.connect(
    f'postgresql://{user}:{pwd}@localhost/autentication'
)

cursor = connect.cursor()