from flask_httpauth import HTTPBasicAuth
from app.models.users import get_user

auth = HTTPBasicAuth('Basic')

@auth.verify_password
def verify_password(username,password):
    if get_user(username,password):
        return username