from model.carrinho import ProdutoCarrinho, Carrinho

import pytest
import requests


class TestCarrinhos:
    """
    Classe de testes do endpoint /produtos
    """

    def test_buscar_produtos(self, get_auth_token, cadastrar_usuario, cadastrar_produto, cadastrar_carrinho, carrinhos_url):
        usuario = cadastrar_usuario(administrador="false")
        auth_token = get_auth_token(usuario['email'], usuario['password'])

        produto = cadastrar_produto()
        produto_carrinho = [ProdutoCarrinho(produto["_id"], 5)]
        carrinho = cadastrar_carrinho(produto_carrinho, auth_token)

        carrinho_esperado = {
            "produtos": [{
                "idProduto": produto["_id"],
                "quantidade": 5,
                "precoUnitario": produto["preco"]
            }],
            "precoTotal": produto["preco"] * 5,
            "quantidadeTotal": 5,
            "idUsuario": usuario["_id"],
            "_id": carrinho["_id"]
        }

        resposta = requests.get(carrinhos_url)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] >= 1
        assert carrinho_esperado in resposta_de_sucesso["carrinhos"]
