from importlib.resources import path
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
import sqlite3
from models.presence import PresenceModel


class Presences(Resource):


    '''
    DATA REQUEST SCHEMA
    '''


    def get(self):
        connection = sqlite3.connect('db.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM presence')


class Presence(Resource):


    '''
    DATA REQUEST SCHEMA
    '''
    arguments = reqparse.RequestParser()
    # arguments.add_argument('presence_id', type=str, required=True, help="Got to have presence id.")
    arguments.add_argument('date_time_sent', type=str, required=True, help="Got to add datetime.")
    arguments.add_argument('sensor_id', type=str, required=True, help="Sensors gotta have a name.")
    arguments.add_argument('detection', type=int, required=True, help="Need to tell if something was detected.")

    '''
    REQUESTS
    '''
    def get(self, presence_id):
        found_presence = PresenceModel.find_presence(presence_id)
        if found_presence:
            return found_presence.json(), 200 # success
        return {'message': 'Presence searched not found.'}, 404 # not found
    
    def post(self):
        data = Presence.arguments.parse_args() # get metadata as dict
        new_presence = PresenceModel(**data)
        print(new_presence.presence_id, new_presence.date_time_received)
        try:
            new_presence.save_presence()
            return new_presence.json(), 200 # success
        except:
            return {'message': 'An internal error ocurred trying to save.'}, 500 # internal server error
    