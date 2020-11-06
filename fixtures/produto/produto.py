from model.produto import Produto

import random
import requests
import pytest


@pytest.fixture(scope='module')
def cadastrar_produto(url_produtos, get_auth_token):

    def _cadastro(preco=random.randint(10, 30000)):
        produto = Produto(preco)

        headers = {"Authorization": f"{get_auth_token()}"}
        response = requests.post(url_produtos, json={
            "nome": produto.nome,
            "preco": produto.preco,
            "descricao": produto.descricao,
            "quantidade": produto.quantidade
        }, headers=headers)

        return {
            "nome": produto.nome,
            "preco": produto.preco,
            "descricao": produto.descricao,
            "quantidade": produto.quantidade,
            '_id': response.json()['_id']
        }
    return _cadastro
