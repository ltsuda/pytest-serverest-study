from model.login import Login
from requests.exceptions import HTTPError

import requests
import pytest


@pytest.fixture(scope='module')
def get_auth_token(login_url, variables):
    credentials = Login(variables['email'], variables['passwd'])
    response = requests.post(login_url, json={
        'email': credentials.email,
        'password': credentials.password
    })
    response.raise_for_status()

    return response.json()['authorization']
