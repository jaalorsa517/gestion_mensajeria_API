from app.models.users import get_user
from flask_restful import Resource,request
from app.auth import auth
from app.models.users import get_user

class Login(Resource):
    
    def post(self):
        username = request.get_json().get('username')
        password = request.get_json().get('password')

        if get_user(username,password):
            return dict(message="Bienvenido", code=200), 200
        else:
            return dict(message="El usuario ingresado no existe", code=401), 401
