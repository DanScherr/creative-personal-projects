import os

# gerando senha aleatória
secret_key_maker = str(os.urandom(16))

# abrindo e lendo arquivo dotenv
with open(".env", mode='r') as file:
    dotenv_passado = file.readlines()

# atribuindo a uma variável a string que queremos substituir
str_de_substituicao = dotenv_passado[1][len('SECRET_KEY='):]

# substituindo a string que queremos pela senha aleatoria gerada
dotenv_passado[1] = dotenv_passado[1].replace(str_de_substituicao, secret_key_maker + '\n')

# realizando ultima tratativa na string de substituição
str_de_substituicao = ''.join(dotenv_passado)

# re-escrevendo arquivo .env com a variavel aleatoria
with open(".env", mode='w') as dotenv_atualizado:
    dotenv_atualizado.write(str_de_substituicao)

