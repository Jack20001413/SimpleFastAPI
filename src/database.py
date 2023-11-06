from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from azure.appconfiguration.provider import load
import os

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456@localhost:5432/Student"

config = load(connection_string=os.environ.get("AZURE_APPCONFIG_CONNECTION_STRING"))
if config["postgres_conn"]:
    SQLALCHEMY_DATABASE_URL = str(config["postgres_conn"])

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
