from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..base import Base


class FilmType(Base):
    __tablename__ = 'film_types'

    film_type_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    films = relationship(
        'Film',
        backref='film_types',
        cascade='all, delete',
        passive_deletes=True
    )

    def to_dict(self):
        return {
            'film_type_id': self.film_type_id,
            'name': self.name
        }
