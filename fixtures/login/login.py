from model.login import Login

import requests
import pytest


@pytest.fixture(scope='function')
def get_auth_token(login_url, variables):

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

        response = requests.post(login_url, json=data)
        response.raise_for_status()
        return response.json()['authorization']

    return _login
