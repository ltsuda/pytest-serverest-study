from model import Produto
from model import ProdutoCarrinho, Carrinho
from copy import copy

import pytest
import random
import requests


class TestPOSTProdutos:
    """
    Suite de testes do endpoint /produtos e método POST
    """

    @pytest.fixture(autouse=True)
    def setup_produto(self, request, cadastrar_produto, cadastrar_usuario):
        if 'usuario_comum' in request.keywords:
            self.usuario = cadastrar_usuario(administrador="false")
        else:
            self.produto = cadastrar_produto()

    def test_cadastrar_produto(self, url_produtos, get_auth_token):
        produto = Produto()

        headers = {"Authorization": f"{get_auth_token()}"}

        resposta = requests.post(url_produtos, json={
            "nome": produto.nome,
            "preco": produto.preco,
            "descricao": produto.descricao,
            "quantidade": produto.quantidade
        }, headers=headers)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 201
        assert resposta_de_sucesso["message"] == "Cadastro realizado com sucesso"
        assert "_id" in resposta_de_sucesso

    def test_cadastrar_produto_ja_existente(self, faker, url_produtos, get_auth_token):
        headers = {"Authorization": f"{get_auth_token()}"}

        resposta = requests.post(
            url_produtos, json={
                "nome": self.produto["nome"],
                "preco": random.randint(10, 30000),
                "descricao": faker.sentence(),
                "quantidade": random.randint(1, 1000)
            }, headers=headers)

        resposta_de_erro = resposta.json()
        assert resposta.status_code == 400
        assert resposta_de_erro["message"] == "Já existe produto com esse nome"

    def test_cadastrar_produto_com_token_invalido(self, faker, url_produtos):
        produto = Produto()

        headers = {"Authorization": f"{faker.uuid4()}"}

        resposta = requests.post(
            url_produtos, json={
                "nome": produto.nome,
                "preco": produto.preco,
                "descricao": produto.descricao,
                "quantidade": produto.quantidade
            }, headers=headers)

        resposta_de_erro = resposta.json()
        assert resposta.status_code == 401
        assert resposta_de_erro["message"] == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"

    @pytest.mark.usuario_comum
    def test_cadastrar_produto_com_usuario_comum(self, url_produtos, url_login):
        resposta = requests.post(url_login, json={
            "email": self.usuario["email"],
            "password": self.usuario["password"]
        })
        resposta_de_sucesso = resposta.json()

        produto = Produto()

        headers = {"Authorization": f'{resposta_de_sucesso["authorization"]}'}

        resposta = requests.post(
            url_produtos, json={
                "nome": produto.nome,
                "preco": produto.preco,
                "descricao": produto.descricao,
                "quantidade": produto.quantidade
            }, headers=headers)

        resposta_de_erro = resposta.json()
        assert resposta.status_code == 403
        assert resposta_de_erro["message"] == "Rota exclusiva para administradores"
