from datetime import datetime

from flask import request, make_response

from db import session_scope, tables
from .app import app


@app.route('/', methods=['GET'])
def film_types_list():
    with session_scope() as session:
        types_list = session.query(tables.FilmType).all()
        return {
            'film types': [ftype.to_dict() for ftype in types_list]
        }


@app.route('/<film_type_id>', methods=['GET', 'POST'])
def film_list(film_type_id):
    with session_scope() as session:
        if request.method == 'GET':
            film_type = session.query(tables.FilmType).filter(
                tables.FilmType.film_type_id == film_type_id
            ).first()

            return {
                'type': film_type.name,
                'films': [film.to_dict() for film in film_type.films]
            }
