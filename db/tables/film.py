from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..base import Base


class Film(Base):
    __tablename__ = 'films'

    film_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
    film_type_id = Column(
        Integer, ForeignKey('film_types.film_type_id', ondelete="CASCADE")
    )
    actors = relationship("Actor",
                          secondary='films_has_actors',
                          backref="films",
                          cascade="all, delete",
                          passive_deletes=True)
    countries = relationship("Country",
                             secondary='films_has_countries',
                             backref="films",
                             cascade="all, delete",
                             passive_deletes=True)
    genres = relationship("Genre",
                          secondary='films_has_genres',
                          backref="films",
                          cascade="all, delete",
                          passive_deletes=True)

    def to_dict(self):
        return {
            'film_type_id': self.film_type_id,
            'film_id': self.film_id,
            'title': self.title,
            'year': self.year,
            'duration': self.duration,
            'rating': self.rating,
            'actors': [actor.to_dict() for actor in self.actors],
            'countries': [country.to_dict() for country in self.countries],
            'genres': [genre.to_dict() for genre in self.genres]
        }
