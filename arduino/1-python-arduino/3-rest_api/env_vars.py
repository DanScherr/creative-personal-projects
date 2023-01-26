'''
    This file contains the environmental variables
    that will be imported in app.py and used for
    the relative configuration of the Flask app
    object for the JWT Manager.
'''
from dotenv import dotenv_values

env_vars = dotenv_values("./.env")

jwt_secret_key = env_vars['JWT_SECRET_KEY']
jwt_algorithm = env_vars['JWT_ALGORITHM']