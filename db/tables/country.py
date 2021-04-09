from sqlalchemy import Column, Integer, String

from ..base import Base


class Country(Base):
    __tablename__ = 'countries'

    country_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
