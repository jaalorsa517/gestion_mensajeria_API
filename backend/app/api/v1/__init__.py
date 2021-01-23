from app.api import api

from .resources.signin import Signin
from .resources.login import Login
from .resources.deliveries import Deliveries
from .resources.test import Test

api.add_resource(Signin,'/signin',endpoint='signin')
api.add_resource(Login,'/login',endpoint='login')
api.add_resource(Deliveries,'/deliveries',endpoint='deliveries')
api.add_resource(Test,'/')

