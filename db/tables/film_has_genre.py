from sqlalchemy import Column, Integer, ForeignKey

from ..base import Base


class FilmHasGenre(Base):
    __tablename__ = 'films_has_genres'

    film_id = Column(Integer,
                     ForeignKey('films.film_id', ondelete="CASCADE"),
                     primary_key=True)
    genre_id = Column(Integer,
                      ForeignKey('genres.genre_id', ondelete="CASCADE"),
                      primary_key=True)
