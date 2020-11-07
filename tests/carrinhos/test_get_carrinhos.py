from model import ProdutoCarrinho

import random
import requests
import pytest


class TestGETCarrinhos:
    """
    Suite de testes do endpoint /carrinhos e método GET
    """

    @pytest.fixture(autouse=True)
    def setup_produto(self, get_auth_token, cadastrar_produto, cadastrar_carrinho, cadastrar_usuario):
        usuario = cadastrar_usuario(administrador="false")

        auth_token = get_auth_token(
            usuario['email'], usuario['password'])
        produto = cadastrar_produto()
        quantidade_produto = random.randint(1, 10)
        produto_carrinho = [ProdutoCarrinho(
            produto["_id"], quantidade_produto)]
        self.carrinho = cadastrar_carrinho(
            produto_carrinho, auth_token)

        self.carrinho_esperado = {
            "produtos": [{
                "idProduto": produto["_id"],
                "quantidade": quantidade_produto,
                "precoUnitario": produto["preco"]
            }],
            "precoTotal": produto["preco"] * quantidade_produto,
            "quantidadeTotal": quantidade_produto,
            "idUsuario": usuario["_id"],
            "_id": self.carrinho["_id"]
        }

    def test_buscar_carrinhos(self, url_carrinhos):
        resposta = requests.get(url_carrinhos)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] >= 1
        assert self.carrinho_esperado in resposta_de_sucesso["carrinhos"]

    def test_buscar_carrinho_por_id(self, url_carrinhos):
        query = f'?_id={self.carrinho["_id"]}'
        resposta = requests.get(url_carrinhos + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] == 1
        assert self.carrinho_esperado == resposta_de_sucesso["carrinhos"][0]

    def test_buscar_carrinho_por_preco_total(self, url_carrinhos):
        query = f'?precoTotal={self.carrinho_esperado["precoTotal"]}'
        resposta = requests.get(url_carrinhos + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] >= 1
        assert self.carrinho_esperado in resposta_de_sucesso["carrinhos"]

    def test_buscar_carrinho_por_quantidade_total(self, url_carrinhos):
        query = f'?quantidadeTotal={self.carrinho_esperado["quantidadeTotal"]}'
        resposta = requests.get(url_carrinhos + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] >= 1
        assert self.carrinho_esperado in resposta_de_sucesso["carrinhos"]

    def test_buscar_carrinho_por_id_do_usuario(self, url_carrinhos):
        query = f'?idUsuario={self.carrinho_esperado["idUsuario"]}'
        resposta = requests.get(url_carrinhos + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] == 1
        assert self.carrinho_esperado == resposta_de_sucesso["carrinhos"][0]

    def test_buscar_carrinho_por_id_e_preco_total(self, url_carrinhos):
        query = f'?_id={self.carrinho_esperado["_id"]}&precoTotal={self.carrinho_esperado["precoTotal"]}'
        resposta = requests.get(url_carrinhos + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] == 1
        assert self.carrinho_esperado == resposta_de_sucesso["carrinhos"][0]
