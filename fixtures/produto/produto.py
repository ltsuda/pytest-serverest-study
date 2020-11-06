from model import Produto

import random
import requests
import pytest


@pytest.fixture(scope='module')
def cadastrar_produto(url_produtos, get_auth_token):
    """Fixture que retorna o método de cadastro de um produto

        Args:
            url_produtos (fixture[str]): URL completa do endpoint de produtos
            get_auth_token (fixture[str]): Bearer token para autenticação retornado pela fixture
    """

    def _cadastro(preco=random.randint(10, 30000)):
        """Cria um produto e realiza o cadastro no servidor

        Args:
            preco (int, optional): Preço do produto (aleátorio por padrão)

        Returns:
            (dict) = Dicionário com os dados do produto cadastrado
        """
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
