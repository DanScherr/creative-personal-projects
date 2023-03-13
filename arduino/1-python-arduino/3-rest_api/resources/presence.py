from models.presence import PresenceModel
from flask_restful import Resource, reqparse
from importlib.resources import path
import sqlite3
from flask_jwt_extended import jwt_required
from models.sensor import SensorModel
from resources.query_filters.presence import normalize_path_params, consulta_sem_sensorid, consulta_com_sensorid


path_params = reqparse.RequestParser()
path_params.add_argument('sensor_id', type=str, location='values')
path_params.add_argument('year_min', type=int, location='values')
path_params.add_argument('month_min', type=int, location='values')
path_params.add_argument('day_min', type=int, location='values')
path_params.add_argument('hour_min', type=int, location='values')
path_params.add_argument('minute_min', type=int, location='values')
path_params.add_argument('second_min', type=int, location='values')
path_params.add_argument('year_max', type=int, location='values')
path_params.add_argument('month_max', type=int, location='values')
path_params.add_argument('day_max', type=int, location='values')
path_params.add_argument('hour_max', type=int, location='values')
path_params.add_argument('minute_max', type=int, location='values')
path_params.add_argument('second_max', type=int, location='values')


class Presences(Resource):


    def get(self):
        connection = sqlite3.connect('./instance/database.db')
        cursor = connection.cursor()
        data = path_params.parse_args()
        print(data)
        valid_data = { key:data[key] for key in data if data[key] is not None }
        params = normalize_path_params(**valid_data)

        if not params.get('sensor_id'):
            params_tuple = tuple([ params[key] for key in params ])
            query = cursor.execute(consulta_sem_sensorid, params_tuple)
        else:
            params_tuple = tuple([ params[key] for key in params ])
            query = cursor.execute(consulta_com_sensorid, params_tuple)
        print(params_tuple)
        presences = []

        for column in query:
            presences.append(
                {
                    'sensor_id'             : column[0],
                    'detection'             : column[1],
                    'date_time_sent'        : column[2],
                    'year'                  : column[3],
                    'month'                 : column[4],
                    'day'                   : column[5],
                    'hour'                  : column[6],
                    'minute'                : column[7],
                    'second'                : column[8]
                    
                }
            )

        return presences
    
    def delete(self):
        connection = sqlite3.connect('./instance/database.db')
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
    