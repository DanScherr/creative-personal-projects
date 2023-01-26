''' 
    This file will create the SQLAlchemy data-base.
        It will be called on app.py
        Its schema will be defined on ./models/
'''
# ----- imports -----
# 1. importando SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
