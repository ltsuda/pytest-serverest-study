from model.login import Login

import requests
import pytest


@pytest.fixture(scope='module')
def get_auth_token(login_url, variables):
    credentials = Login(variables['email'], variables['passwd'])
    response = requests.post(login_url, json={
        'email': credentials.email,
        'password': credentials.password
    })
    return response.json()['authorization']
