from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from backend.library_app.config import setting


engine = create_engine(setting.database_url, connect_args={"check_same_thread": False})

Base = declarative_base()

session_factory = sessionmaker(bind=engine, autoflush=False)

def get_bd():
    db = session_factory()
    try:
        yield db
    finally:
        db.close()

def init_db():
     Base.metadata.create_all(bind=engine)
#init_db()

