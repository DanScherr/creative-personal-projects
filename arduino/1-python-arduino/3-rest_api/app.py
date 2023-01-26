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
#4 import
from blocklist import BLOCKLIST


'''
CONFIGURE
'''
# from 1st import -> config for FLask application
app = Flask(__name__)
api = Api(app)
# from 1st import -> config for SQL_ALCHEMY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db' # configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # configurar como false tracking de modificações
# from 1.1st import -> config for JWT
app.config['JWT_SECRET_KEY'] = jwt_secret_key # configurando chave do lado da aplicação
app.config['JWT_ALGORITHM'] = jwt_algorithm # configuring app to have HS256 as the algorithym password
app.config['JWT_BLACKLIST_ENABLED'] = True # enabling the blocklist to validate the users
# from 2nd import -> instancying jwt manager
jwt = JWTManager(app)


'''
EVENT-DRIVEN DECORATORS
'''
# decorator for before first API request
@app.before_first_request
def create_database():
    # from 3rd import -> instanciates and creates database
    db.create_all() # before first request, database will be created
# decorator to verify if user id is in blacklist
@jwt.token_in_blocklist_loader
def verifies_blocklist(self, token):
    # from 4th import -> checks blocklist
    return token['jti'] in BLOCKLIST
# decorator to respond in case in blocklist
@jwt.revoked_token_loader
def invalid_access_token(jwt_header, jwt_payload):
    return jsonify({"message": "You have been logged out."}), 401 # unauthorized


'''
ADDING RESOURCES
'''



'''
MAIN CONTEXT
'''
if __name__ == '__main__':
    # 3 import
    from sql_alchemy import db
    app.run(debug=True)