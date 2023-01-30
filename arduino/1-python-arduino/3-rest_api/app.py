'''
IMPORT
'''
# 1 import.
from flask import Flask, jsonify
from flask_restful import Api
# 1.1 import
from env_vars import jwt_secret_key, jwt_algorithm
# 2 import
from flask_jwt_extended import JWTManager
# 4 import
from blocklist import BLOCKLIST
# 5 import
from resources.presence import Presence
from resources.presence import Presences
from resources.sensor import Sensor
from resources.sensor import SensorRegister


'''
CONFIGURE
'''
app = Flask(__name__) # from 1st import -> config for FLask application
api = Api(app) # from 1st import -> config for SQL_ALCHEMY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db' # configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # configurar como false tracking de modificações
app.config['JWT_SECRET_KEY'] = jwt_secret_key # configurando chave do lado da aplicação
app.config['JWT_ALGORITHM'] = jwt_algorithm # from 1.1st import -> config for JWT # configuring app to have HS256 as the algorithym password
app.config['JWT_BLACKLIST_ENABLED'] = True # enabling the blocklist to validate the users
jwt = JWTManager(app) # from 2nd import -> instancying jwt manager


'''
EVENT-DRIVEN DECORATORS
'''
@app.before_first_request
def create_database():
    # from 3rd import -> instanciates and creates database
    db.create_all() # before first request, database will be created

@jwt.token_in_blocklist_loader # decorator to verify if user id is in blacklist
def verifies_blocklist(self, token):
    return token['jti'] in BLOCKLIST # from 4th import -> checks blocklist

@jwt.revoked_token_loader # decorator to respond in case in blocklist
def invalid_access_token(jwt_header, jwt_payload):
    return jsonify({"message": "You have been logged out."}), 401 # unauthorized


'''
ADDING RESOURCES
'''
api.add_resource(Presences, '/presences')
api.add_resource(Presence, '/presence')
api.add_resource(Sensor, '/sensor/<string:sensor_id>')
api.add_resource(SensorRegister, '/sensor_register')


'''
MAIN CONTEXT
'''
if __name__ == '__main__':
    # 3 import
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)