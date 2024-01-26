from sqlalchemy import Column, Integer, String
from database.database import Base


class NoteModel(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
