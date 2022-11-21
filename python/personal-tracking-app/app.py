'''
    app.py é o arquivo da própria aplicação.
    O qual se criará as instâncias e configurações necessárias para se rodá-la.
'''
# 0. Imports
# 1
from flask import Flask, jsonify
from dotenv import dotenv_values
# 2
from flask_restful import Api
# 3
from flask_jwt_extended import JWTManager
# 4
from blocklist import BLOCKLIST


# 1. Instanciamento da aplicação
app = Flask(__name__)
#   1.I. Realizando configurações para a aplicação
#       1.I.i. Configurações de banco de dados
#           1.I.i.a. The database URI that should be used for the connection.
dotenv = dotenv_values(".env")
app.config['SQLALCHEMY_DATABASE_URI'] = dotenv['SECRET_KEY']
#       1.I.ii. Desativando rastreamento da aplicação para não sobrecarregá-la
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#   1.II.Configurações do gerenciador de logins

app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config["JWT_ALGORITHM"] = "HS256"
app.config['JWT_BLACKLIST_ENABLED'] = True

# 2. Instanciamento da api passando a aplicação em Flask como parâmetro
api = Api(app)


# 3. Instanciando gerenciador de Login de usuário
jwt = JWTManager(api)


# 4. Decoradores que indicarão os estados da aplicação
#   4.I. O que fazer antes da primeira requisição à api 
#       4.I.i. Criar banco de dados
@app.before_first_request
def create_banco():
    banco.create_all()

#   4.II. Configurar id de usuário em Blocklist no logout do usuario
#       4.II.i Verifica se o id está na blocklist
@jwt.token_in_blocklist_loader
def verifica_blocklist(self, token):
    return token['jti'] in BLOCKLIST
#       4.II.ii Resposta caso o id verificado estiver na blocklist
@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    return jsonify({"message": "You have been logged out."}), 401 # unauthorized


# 5. Criando recursos da API


if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    # run app on local host
    app.run(host='0.0.0.0', debug=True, port='5000')