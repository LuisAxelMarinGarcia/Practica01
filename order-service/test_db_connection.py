import os
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
database_name = os.getenv('DB_NAME')

if not all([username, password, database_name]):
    raise ValueError("Las variables de entorno DB_USER, DB_PASS y/o DB_NAME no están definidas.")

escaped_password = quote_plus(password)
DATABASE_URL = f'postgresql://{username}:{escaped_password}@localhost:5432/{database_name}'

try:
    engine = create_engine(DATABASE_URL, echo=True)
    connection = engine.connect()
    print("Conexión exitosa a la base de datos")
    connection.close()
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
