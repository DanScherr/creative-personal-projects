''' 
    este documento servirá para criação do objeto banco que o sql alchemy
    irá utilizar para: 
        instanciamento do banco de dados, configurado como sqlite no 
        arquivo app.py e realizado antes da primeira requisição a api
        flask;
'''

from flask_sqlalchemy import SQLAlchemy

# 1. Insancia objeto db do tipo SQLAlchemy
banco = SQLAlchemy()
