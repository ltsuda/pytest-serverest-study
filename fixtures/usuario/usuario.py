from model.usuario import Usuario

import requests
import pytest


@pytest.fixture(scope='function')
def cadastrar_usuario(usuarios_url):

    def _cadastro(administrador="true"):
        usuario = Usuario(administrador)

        response = requests.post(usuarios_url, json={
            'nome': usuario.nome,
            'email': usuario.email,
            'password': usuario.password,
            'administrador': usuario.administrador
        })

        return {
            'nome': usuario.nome,
            'email': usuario.email,
            'password': usuario.password,
            'administrador': usuario.administrador,
            '_id': response.json()['_id']
        }
    return _cadastro
