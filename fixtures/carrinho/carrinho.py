from model import Carrinho

import requests
import pytest


@pytest.fixture(scope='module')
def cadastrar_carrinho(url_carrinhos):
    """Fixture que retorna o método de cadastro de um carrinho

        Args:
            url_carrinhos (str): URL completa do endpoint de carrinhos
    """

    def _cadastro(produtos, user_token):
        """Cria um carrinho de produtos e realiza o cadastro no servidor

        Args:
            produtos (list[ProdutoCarrinho]): Lista de produtos adicionados no carrinho
            user_token (str): Bearer token para autenticação

        Returns:
            (dict) = Dicionário com o ID do carrinho cadastrado
        """
        carrinho = Carrinho(produtos)
        lista_de_produtos = []
        for item in carrinho.produtos:
            produto = {
                "idProduto": item.produto_id,
                "quantidade": item.quantidade
            }
            lista_de_produtos.append(produto)

        headers = {"Authorization": f"{user_token}"}
        response = requests.post(url_carrinhos, json={
            "produtos": lista_de_produtos
        }, headers=headers)
        return {
            "_id": response.json()["_id"]
        }
    return _cadastro
