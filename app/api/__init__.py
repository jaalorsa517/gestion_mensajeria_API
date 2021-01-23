from flask_restful import Api
from app import app

api = Api(app,'/api/v1')

import app.api.v1