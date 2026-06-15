from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user_db_model import Base
from models.pdf_db_model import PDF 

DATABASE_URL = "mysql+pymysql://root:rashi%40123@localhost/studymate_ai"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()