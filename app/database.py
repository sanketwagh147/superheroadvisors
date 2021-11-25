from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
# Syntax for connection
#QLALCHEMY_DATABASE_URL = 'postgressql://<username>:<password>@<ip-address/hostname>/<database_name> 

# No hardcoded password
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)  # Engine responsible for the session

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # Some default values different for 

# import this to alembic .env first
Base = declarative_base()  # to create database

# Dependency
# Get a session for connecting our database and close after requests
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()