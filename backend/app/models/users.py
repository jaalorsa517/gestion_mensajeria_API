""" Modulo que se encarga de gestionar los usuarios"""

from app import app
from csv import DictWriter, DictReader
from os.path import join
from werkzeug.security import check_password_hash


def save_user(username, password):
    with open(
        join(app.instance_path, "app", "data", "users.py"), "a", newline=""
    ) as csv_file:
        write = DictWriter(csv_file, ["user", "password"])

        write.writeheader()
        write.writerow(dict(user=username, password=password))


def get_user(username, password):
    users = []
    with open(
        join(app.instance_path, "app", "data", "users.py"), newline=""
    ) as csv_file:
        reader = DictReader(csv_file)
        users = [user for user in reader]
    if users:
        for user in users:
            if username == user.get("user") and check_password_hash(
                user.get("password"), password
            ):
                return True
    else:
        return False
