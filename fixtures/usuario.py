from model.usuario import Usuario

import requests
import pytest


@pytest.fixture(scope='function')
def cadastrar_usuario(usuarios_url):

    def _cadastro(administrator="true"):
        usuario = Usuario(administrator)

        response = requests.post(usuarios_url, json={
            'nome': usuario.name,
            'email': usuario.email,
            'password': usuario.password,
            'administrador': usuario.administrator
        })

        return {
            'nome': usuario.name,
            'email': usuario.email,
            'password': usuario.password,
            'administrador': usuario.administrator,
            '_id': response.json()['_id']
        }
    return _cadastro
