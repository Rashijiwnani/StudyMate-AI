from models.user_db_model import Base
from sqlalchemy import Column, Integer, String,DateTime
from datetime import datetime

class PDF(Base):
    __tablename__ = "pdfs"

    id = Column(Integer, primary_key=True, autoincrement=True)

    user_id = Column(Integer)

    file_name = Column(String(255))

    file_path = Column(String(500))
    upload_date = Column(DateTime, default=datetime.now)