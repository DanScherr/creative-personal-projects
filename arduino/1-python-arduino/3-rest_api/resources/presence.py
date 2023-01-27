from models.presence import PresenceModel
from flask_restful import Resource, reqparse
from importlib.resources import path
import sqlite3
from flask_jwt_extended import jwt_required
from models.sensor import SensorModel

class Presences(Resource):


    def get(self):
        connection = sqlite3.connect('./instance/banco.db')
        cursor = connection.cursor()
        query = cursor.execute('SELECT * FROM presence;')
        presences = []
        for column in query:
            presences.append(
                {
                    'presence_id'           : column[0],
                    'date_time_sent'        : column[1],
                    'date_time_received'    : column[2],
                    'sensor_id'             : column[3],
                    'detection'             : column[4]
                }
            )
        return presences
    
    def delete(self):
        connection = sqlite3.connect('./instance/banco.db')
        cursor = connection.cursor()
        cursor.execute('DELETE from presence;')
        connection.commit()
        return {'message': 'Data from table deleted.'}


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

    def post(self):
        data = Presence.arguments.parse_args() # get metadata as dict
        sensor_id = data['sensor_id']
        if not SensorModel.find_sensor(sensor_id):
            return {'message': 'The presence must be associated to a valid sensor id.'}, 400
        
        new_presence = PresenceModel(**data)
        try:
            new_presence.save_presence()
            return new_presence.json(), 200 # success
        except:
            return {'message': 'An internal error ocurred trying to save.'}, 500 # internal server error
    