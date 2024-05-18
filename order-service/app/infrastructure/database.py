from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

username = 'root'
password = 'password'  # Cambia esto a la nueva contraseña de tu usuario root
escaped_password = quote_plus(password)
database_name = 'prueba'
host = 'localhost'
port = '3306'  # Puerto predeterminado de MySQL

DATABASE_URL = f'mysql+mysqlconnector://{username}:{escaped_password}@{host}:{port}/{database_name}'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
