from models.sensor import SensorModel
from models.presence import PresenceModel
from flask_restful import Resource, reqparse
from importlib.resources import path
import sqlite3
from flask_jwt_extended import jwt_required


'''
DATA REQUEST SCHEMA
'''
atributes = reqparse.RequestParser()
atributes.add_argument('sensor_id', type=str, required=True, help="Got to add id.")
atributes.add_argument('sensor_name', type=str, required=True, help="Got to add name.")

class Sensor(Resource):


    # criar put

    def delete(self, sensor_id):
        found_sensor = SensorModel.find_sensor(sensor_id)
        if found_sensor:
            try:
                found_sensor.delete_sensor()
                return {'message': 'User deleted.'}, 200
            except:
                return {'message:' 'An internal error ocurred trying to delete user.'}, 500

        return {'message': 'User not found'}, 404
    
class SensorRegister(Resource):


    def post(self):
        data = atributes.parse_args()
        new_sensor = SensorModel(**data)
        print(new_sensor.sensor_id)
        try:
            new_sensor.save_sensor()
            return new_sensor.json(), 200 # success
        except:
            return {'message': 'An internal error ocurred trying to save.'}, 500 # internal server error
        

