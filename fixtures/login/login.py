from model import Login

import requests
import pytest


@pytest.fixture(scope='module')
def get_auth_token(url_login, variables):
    """Fixture que retorna o método de login

        Args:
            url_login (fixture[str]): URL completa do endpoint de login
            variables (dict): Dicionário com configurações carregadas pelo plugin pytest-variables
    """

    def _login(email="", password=""):
        """Realiza o login do usuário no sistema

        Args:
            email (str): Endereço de email do usuário (Vazio por padrão)
            password (str): Senha do usuário (Vazio por padrão)

        Returns:
            (str) =  Bearer token para autenticação
        """
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
