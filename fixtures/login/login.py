from model import Login

import requests
import pytest


@pytest.fixture(scope='module')
def get_auth_token(url_login, variables):

    def _login(email="", password=""):
        data = {
            "email": "",
            "password": ""
        }
        if not email and not password:
            credentials = Login(variables['email'], variables['password'])
            data["email"] = credentials.email
            data["password"] = credentials.password
        else:
            credentials = Login(email, password)
            data["email"] = credentials.email
            data["password"] = credentials.password

        response = requests.post(url_login, json=data)
        response.raise_for_status()
        return response.json()['authorization']

    return _login
