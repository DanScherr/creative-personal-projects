# **CREATIVE PROJECTS:** :books::brain:

<br>

### This is the ***api directory*** of **Arduino with Python** project with **Python**: :mortar_board::closed_book::robot:

<br>

# **SUMÁRIO:** :round_pushpin:

<br>

- # **[Rest API Repository](https://github.com/DanScherr/learning-courses/tree/main/python/api-restful)**


- # **Libraries**:
    1. ```pip install flask-restful``` :arrow_right:
    to access documentation [follow...](https://flask-restful.readthedocs.io/en/latest/installation.html#installation)

        - it's **configured** in [app.py](./app.py) file.

    <br>

    2. ```pip install -U FLask-SQLAlchemy``` :arrow_right:
    to access documentation [follow...](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/)

        - it's **instaciated** in [sql_alchemy.py](./sql_alchemy.py) file and **imported** in [app.py](./app.py) file at the end of it (after the ```if __name__ == '__main__':``` clause).

    3. ```pip install Flask-JWT-Extended``` :arrow_right:
    to access documentation [follow...](https://flask-jwt-extended.readthedocs.io/en/stable/)
        - it's **used on** [app.py](./app.py) with **python decorator structure**<sup>[#](https://peps.python.org/pep-0318/)</sup> code to manage user login and authentification.

- # Flask:
    - instaciate Flask app on [app.py](./app.py).
    - instanciate Flask API on [app.py](./app.py).
    - gotta make some configurations relativelly to the app instance folder on [app.py](./app.py).
    - calls app to run in Main Context (after the ```if __name__ == '__main__':``` clause).
    - Add resources on [app.py](./app.py)

- # SQLAlchemy:
    - create a side file (in order to make it more organised) named [sql_alchemy.py](./sql_alchemy.py) that instanciates a database and to be imported on [app.py](./app.py) file to create the data base when called.
    - import library (file) in Main Context (after the ```if __name__ == '__main__':``` clause) 
    - gotta make some configurations relativelly to the app instance folder on [app.py](./app.py).
    - create an event-driven decorator on [app.py](./app.py) so that the data-base will be created before first request.

- # JWT Manager:
    - gotta make some configurations relativelly to the app instance folder on [app.py](./app.py).
        - ## .env file:
            - to make the JWT password and type of encriptying safer, we will create a .env file to load the environmental variables.
            - create a [env_vars.py](./env_vars.py) side file (for organization purpose) to work with the .env file and create the variables that will be imported in [app.py](./app.py) for the configuration of the JWT.

    - ## BLOCKLIST:
        - create a side file [blocklist.py](./blocklist.py) to create an unordered collection with no duplicate elements to validate user id login with [set()](https://docs.python.org/3/tutorial/datastructures.html) function.

    - create an event-driven decorator on [app.py](./app.py) so that the app verifies token in blocklist.

- # Model:


- # ADD Resources:
    - Add resources structure in [app.py](./app.py) following the business rules mapped.
    - ## POSTMAN (optional):
        - Configure Headers:

            ![postman header configuration](./../images/post-man-json-config.png)

        - Create requests for the resources to test them:

            ![](./../images/postman-post-request-sucessfull.png)

        - View in the database created the new table and post:

            ![](./../images/sqlite-first-sucess-post.png)
        

- # Models:
    - Located in [./models/](./models/)
    - For each resource, create a file .py
        - In each file, build Classes with its atributes and methods of the entity resource of the api.
    1. Create Class (POO).
    2. Create the table schema to be added to the database object (must import it at the beginning of the file).
    3. Create the Class constructor together with its methods that are going to interact with the database e give back its metadata.

- # Resources:
    - Located in [./resources/](./resources/)
    - For each resource create a file.
        - In each file, build Classes with its atributes and methods (get, put, post, delete).
    - Every file and its respectives classes must be imported on [app.py](./app.py) and added into the api object resource.




<br>

***

<br>

- ### **Please, be welcome to check my profile:** :nerd_face::handshake:

<br>

<a href="https://github.com/DanScherr">
    <img src="./../images/the-end-img.png" width="50%">
</a>


