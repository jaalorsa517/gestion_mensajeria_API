from flask_restful import Resource
from flask_cors import cross_origin

class Test (Resource):
    decorators=[cross_origin]
    def get(self):
        return {"Prueba":"url test"},200