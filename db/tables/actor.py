from sqlalchemy import Column, Integer, String, DateTime

from ..base import Base


class Actor(Base):
    __tablename__ = 'actors'

    actor_id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=True)
    birthdate = Column(DateTime, nullable=True)
