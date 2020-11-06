from model.carrinho import ProdutoCarrinho, Carrinho

import requests
import pytest


@pytest.fixture(scope='module')
def cadastrar_carrinho(url_carrinhos):

    def _cadastro(produtos, user_token):
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
