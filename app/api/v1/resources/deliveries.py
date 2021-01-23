from flask_restful import Resource, request
from app.auth import auth
from app.models.delivery import get_deliveries, save_delivery


class Deliveries(Resource):
    decorators = [auth.login_required]

    def get(self):
        return dict(data=get_deliveries()), 200

    def patch(self):
        delivery = request.get_json().get('delivery')
        available = request.get_json().get('available')
        if save_delivery(delivery, available):
            return dict(message='Recurso actualizado'), 201
        else:
            return dict(message='Hubo un error al guardar'), 401
