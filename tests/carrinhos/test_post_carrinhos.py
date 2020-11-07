from model import ProdutoCarrinho, Carrinho

from copy import copy

import random
import requests
import pytest


class TestPOSTCarrinhos:
    """
    Suite de testes do endpoint /carrinhos e método POST
    """

    @pytest.fixture(autouse=True)
    def setup_carrinho(self, get_auth_token, cadastrar_produto, cadastrar_usuario):
        usuario = cadastrar_usuario(administrador="false")
        self.auth_token = get_auth_token(
            usuario['email'], usuario['password'])
        self.headers = {"Authorization": f"{self.auth_token}"}

        self.produto = cadastrar_produto()
        quantidade_produto = random.randint(1, 10)
        carrinho = Carrinho([ProdutoCarrinho(
            self.produto["_id"], quantidade_produto)])

        self.lista_de_produtos = []
        for item in carrinho.produtos:
            produto_carrinho = {
                "idProduto": item.produto_id,
                "quantidade": item.quantidade
            }
            self.lista_de_produtos.append(produto_carrinho)

    def test_cadastrar_carrinho(self, url_carrinhos):
        resposta = requests.post(url_carrinhos, json={
            "produtos": self.lista_de_produtos
        }, headers=self.headers)

        resposta_de_sucesso = resposta.json()

        assert resposta.status_code == 201
        assert resposta_de_sucesso["message"] == "Cadastro realizado com sucesso"
        assert "_id" in resposta_de_sucesso

    def test_cadastrar_carrinho_com_produto_duplicado(self, url_carrinhos):
        lista_com_duplicados = copy(self.lista_de_produtos)
        lista_com_duplicados.append(self.lista_de_produtos[0])
        resposta = requests.post(url_carrinhos, json={
            "produtos": lista_com_duplicados
        }, headers=self.headers)

        resposta_de_erro = resposta.json()

        assert resposta.status_code == 400
        assert resposta_de_erro["message"] == "Não é permitido possuir produto duplicado"
        assert self.produto["_id"] == resposta_de_erro["idProdutosDuplicados"][0]

    def test_cadastrar_mais_de_um_carrinho_por_usuario(self, url_carrinhos):
        resposta = requests.post(url_carrinhos, json={
            "produtos": self.lista_de_produtos
        }, headers=self.headers)
        assert resposta.status_code == 201

        resposta = requests.post(url_carrinhos, json={
            "produtos": self.lista_de_produtos
        }, headers=self.headers)

        resposta_de_erro = resposta.json()

        assert resposta.status_code == 400
        assert resposta_de_erro["message"] == "Não é permitido ter mais de 1 carrinho"

    def test_cadastrar_carrinho_com_produto_inexistente(self, faker, url_carrinhos):
        produto = {
            "idProduto": faker.uuid4(),
            "quantidade": random.randint(1, 10)
        }
        self.lista_de_produtos.append(produto)

        resposta = requests.post(url_carrinhos, json={
            "produtos": self.lista_de_produtos
        }, headers=self.headers)

        resposta_de_erro = resposta.json()

        assert resposta.status_code == 400
        assert resposta_de_erro["message"] == "Produto não encontrado"
        assert resposta_de_erro["item"]["idProduto"] == produto["idProduto"]
        assert resposta_de_erro["item"]["quantidade"] == produto["quantidade"]

    def test_cadastrar_carrinho_quantidade_produto_insuficiente(self, url_carrinhos):
        self.lista_de_produtos[0]["quantidade"] = 999_999

        resposta = requests.post(url_carrinhos, json={
            "produtos": self.lista_de_produtos
        }, headers=self.headers)

        resposta_de_erro = resposta.json()

        assert resposta.status_code == 400
        assert resposta_de_erro["message"] == "Produto não possui quantidade suficiente"
        assert resposta_de_erro["item"]["idProduto"] == self.produto["_id"]
        assert resposta_de_erro["item"]["quantidade"] == self.lista_de_produtos[0]["quantidade"]
        assert resposta_de_erro["item"]["quantidadeEstoque"] == self.produto["quantidade"]

    def test_cadastrar_carrinho_com_token_invalido(self, faker, url_carrinhos):
        headers = {"Authorization": f"{faker.uuid4()}"}
        resposta = requests.post(url_carrinhos, json={
            "produtos": self.lista_de_produtos
        }, headers=headers)

        resposta_de_erro = resposta.json()

        assert resposta.status_code == 401
        assert resposta_de_erro["message"] == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"
