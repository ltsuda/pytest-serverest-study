from model.login import Login

import requests
import pytest


@pytest.fixture(scope='function')
def get_auth_token(login_url, variables):
    credentials = Login(variables['email'], variables['password'])
    response = requests.post(login_url, json={
        'email': credentials.email,
        'password': credentials.password
    })
    response.raise_for_status()

    return response.json()['authorization']
