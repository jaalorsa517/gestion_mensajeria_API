from app.api import api

from .resources.signin import Signin
from .resources.deliveries import Deliveries

api.add_resource(Signin,'/signin',endpoint='signin')
api.add_resource(Deliveries,'/deliveries',endpoint='deliveries')
