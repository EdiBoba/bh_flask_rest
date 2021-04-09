from sqlalchemy import Column, Integer, ForeignKey

from ..base import Base


class FilmHasCountry(Base):
    __tablename__ = 'films_has_countries'

    film_id = Column(Integer,
                     ForeignKey('films.film_id', ondelete="CASCADE"),
                     primary_key=True)
    country_id = Column(Integer,
                        ForeignKey('countries.country_id', ondelete="CASCADE"),
                        primary_key=True)
