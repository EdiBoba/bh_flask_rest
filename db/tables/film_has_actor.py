from sqlalchemy import Column, Integer, ForeignKey

from ..base import Base


class FilmHasActor(Base):
    __tablename__ = 'films_has_actors'

    film_id = Column(Integer,
                     ForeignKey('films.film_id', ondelete="CASCADE"),
                     primary_key=True)
    actor_id = Column(Integer,
                      ForeignKey('actors.actor_id', ondelete="CASCADE"),
                      primary_key=True)
