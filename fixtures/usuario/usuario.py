from model.usuario import Usuario

import requests
import pytest


@pytest.fixture(scope='module')
def cadastrar_usuario(url_usuarios):

    def _cadastro(administrador="true"):
        usuario = Usuario(administrador)

        response = requests.post(url_usuarios, json={
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
