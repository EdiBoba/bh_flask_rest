from datetime import datetime

from flask import request, make_response

from db import session_scope, tables
from .app import app


@app.route('/actors', methods=['GET', 'POST'])
def actors_list():
    with session_scope() as session:
        if request.method == 'GET':
            actors = session.query(tables.Actor).all()
            result = {
                'actors': [actor.to_dict() for actor in actors]
            }
            return result
        else:
            request_data = request.get_json(force=True)

            birthday = datetime.strptime(
                request_data['birthday'], '%Y-%m-%d'
            ) if request_data.get('birthday') else None

            new_actor = tables.Actor(
                surname=request_data['surname'],
                name=request_data['name'],
                lastname=request_data.get('lastname'),
                birthdate=birthday
            )
            session.add(new_actor)
            session.commit()
            response = make_response({'message': 'actor created'}, 201)
            response.headers['Location'] = f"/actors/{new_actor.actor_id}"
            return response


@app.route('/actors/<actor_id>', methods=['GET', 'PUT', 'DELETE'])
def actor(actor_id):
    with session_scope() as session:
        actor_obj = session.query(
            tables.Actor
        ).filter_by(actor_id=actor_id).first()
        if request.method == 'GET':
            return actor_obj.to_dict()
        elif request.method == 'DELETE':
            actor_obj = session.query(tables.Actor)
            session.delete(actor_obj)
            return {'message': 'actor deleted'}
        else:
            request_data = request.get_json(force=True)

            birthday = datetime.strptime(
                request_data['birthday'], '%Y-%m-%d'
            ) if request_data.get('birthday') else None

            actor_obj.name = request_data['surname']
            actor_obj.name = request_data['name']
            actor_obj.name = request_data.get('lastname')
            actor_obj.birthday = birthday
            return {'message': 'actor updated'}
