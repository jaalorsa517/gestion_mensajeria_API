from flask import Flask

app = Flask(__name__)
from flask_cors import CORS
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

from .api import api
