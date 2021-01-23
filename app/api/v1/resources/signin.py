from flask_restful import Resource, request
from app.models.users import save_user


class Signin (Resource):

    def post(self):
        username = request.get_json().get('username')
        password = request.get_json().get('password')

        if save_user(username, password):

            return dict(message="Se creó el recurso", code=201), 201

        else:

            return dict(message="El usuario ya existe", code=401), 401
            
