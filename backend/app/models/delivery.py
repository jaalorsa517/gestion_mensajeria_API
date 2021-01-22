"""Módulo que se encarga de gestionar los mensajeros"""

from csv import DictReader, DictWriter
from os import write
from os.path import join
from app import app


def get_deliveries():
    with open(
        join(app.instance_path, "app", "data", "users.py"), newline=""
    ) as csv_file:
        reader = DictReader(csv_file)
        if reader:
            return [delivery for delivery in reader]
        else:
            return False

def save_delivery(delivery,available):
    deliveries = get_deliveries()
    if deliveries:
        for index,delivery_ in enumerate(deliveries):
            if delivery == delivery_.get('delivery'):
                deliveries[index].setdefault('available',available)
                break        
        with open(
            join(app.instance_path, "app", "data", "users.py"), "w", newline=""
        ) as csv_file:

            writer = DictWriter(csv_file,['delivery','available'])
            writer.writeheader()
            writer.writerows(deliveries)
