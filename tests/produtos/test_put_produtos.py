from model import Produto
from copy import copy

import random
import requests
import pytest


class TestPUTProdutos:
    """
    Suite de testes do endpoint /produtos e método PUT
    """

    @pytest.fixture(autouse=True)
    def setup_produto(self, request, cadastrar_produto, cadastrar_usuario):
        if 'usuario_comum' in request.keywords:
            self.usuario = cadastrar_usuario(administrador="false")
            self.produto = cadastrar_produto()
        else:
            self.produto = cadastrar_produto()

    def test_editar_produto(self, url_produtos, get_auth_token):
        produto_modificado = copy(self.produto)
        produto_modificado["preco"] = random.randint(10, 30000)

        headers = {"Authorization": f"{get_auth_token()}"}

        resposta = requests.put(
            url_produtos + f'/{self.produto["_id"]}', json={
                "nome": produto_modificado["nome"],
                "preco": produto_modificado["preco"],
                "descricao": produto_modificado["descricao"],
                "quantidade": produto_modificado["quantidade"]
            }, headers=headers)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["message"] == "Registro alterado com sucesso"

        query = f'?_id={self.produto["_id"]}'
        resposta = requests.get(url_produtos + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["produtos"][0] == produto_modificado

    def test_editar_produto_com_id_nao_encontrado(self, faker, url_produtos, get_auth_token):
        produto = Produto()
        produto_id = faker.uuid4()

        headers = {"Authorization": f"{get_auth_token()}"}

        resposta = requests.put(
            url_produtos + f'/{produto_id}', json={
                "nome": produto.nome,
                "preco": produto.preco,
                "descricao": produto.descricao,
                "quantidade": produto.quantidade
            }, headers=headers)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 201
        assert resposta_de_sucesso["message"] == "Cadastro realizado com sucesso"

    def test_editar_criando_produto_nome_ja_existente(self, faker, url_produtos, get_auth_token):
        produto_modificado = copy(self.produto)
        produto_modificado_id = faker.uuid4()
        produto_modificado["preco"] = random.randint(10, 30000)

        headers = {"Authorization": f"{get_auth_token()}"}

        resposta = requests.put(
            url_produtos + f'/{produto_modificado_id}', json={
                "nome": produto_modificado["nome"],
                "preco": produto_modificado["preco"],
                "descricao": produto_modificado["descricao"],
                "quantidade": produto_modificado["quantidade"]
            }, headers=headers)

        resposta_de_erro = resposta.json()
        assert resposta.status_code == 400
        assert resposta_de_erro["message"] == "Já existe produto com esse nome"

    def test_editar_produto_com_token_invalido(self, faker, url_produtos):
        produto_modificado = copy(self.produto)
        produto_modificado["preco"] = random.randint(10, 30000)

        headers = {"Authorization": f"{faker.uuid4()}"}

        resposta = requests.put(
            url_produtos + f'/{self.produto["_id"]}', json={
                "nome": produto_modificado["nome"],
                "preco": produto_modificado["preco"],
                "descricao": produto_modificado["descricao"],
                "quantidade": produto_modificado["quantidade"]
            }, headers=headers)

        resposta_de_erro = resposta.json()
        assert resposta.status_code == 401
        assert resposta_de_erro["message"] == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"

    @pytest.mark.usuario_comum
    def test_editar_produto_com_usuario_comum(self, url_login, url_produtos):
        resposta = requests.post(url_login, json={
            "email": self.usuario["email"],
            "password": self.usuario["password"]
        })

        resposta_de_sucesso = resposta.json()

        produto_modificado = copy(self.produto)
        produto_modificado["preco"] = random.randint(10, 30000)

        headers = {"Authorization": f"{resposta_de_sucesso['authorization']}"}

        resposta = requests.put(
            url_produtos + f'/{self.produto["_id"]}', json={
                "nome": produto_modificado["nome"],
                "preco": produto_modificado["preco"],
                "descricao": produto_modificado["descricao"],
                "quantidade": produto_modificado["quantidade"]
            }, headers=headers)

        resposta_de_erro = resposta.json()
        assert resposta.status_code == 403
        assert resposta_de_erro["message"] == "Rota exclusiva para administradores"
