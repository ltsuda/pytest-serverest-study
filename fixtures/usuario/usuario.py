from model import Usuario

import requests
import pytest


@pytest.fixture(scope='module')
def cadastrar_usuario(url_usuarios):
    """Fixture que retorna o método de cadastro de um usuário

        Args:
            url_usuarios (fixture[str]): URL completa do endpoint de usuários
    """

    def _cadastro(administrador="true"):
        """Cria um usuário e o registra no servidor

        Args:
            administrador (str, optional): Indica se o usuário é administrador ("false" por padrão)

        Returns:
            (dict) = Dicionário com os dados do usuário cadastrado
        """
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
