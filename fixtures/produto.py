from model.produto import Produto

import random
import requests
import pytest


@pytest.fixture(scope='function')
def cadastrar_produto(produtos_url, get_auth_token):

    def _cadastro(preco=random.randint(10, 30000)):
        usuario = Produto(preco)

        headers = { "Authorization": f"{get_auth_token}" }
        response = requests.post(produtos_url, json={
            "nome": usuario.nome,
            "preco": usuario.preco,
            "descricao": usuario.descricao,
            "quantidade": usuario.quantidade
        }, headers=headers)

        return {
            "nome": usuario.nome,
            "preco": usuario.preco,
            "descricao": usuario.descricao,
            "quantidade": usuario.quantidade,
            '_id': response.json()['_id']
        }
    return _cadastro
