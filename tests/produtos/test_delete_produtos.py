from model import ProdutoCarrinho, Carrinho

import random
import requests
import pytest


class TestDELETEProdutos:
    """
    Suite de testes do endpoint /produtos e método DELETE
    """

    @pytest.fixture(autouse=True)
    def setup_produto(self, request, cadastrar_produto, cadastrar_usuario):
        self.produto = cadastrar_produto()
        if 'usuario_comum' in request.keywords:
            self.usuario = cadastrar_usuario(administrador="false")

    def test_delete_produto(self, url_produtos, get_auth_token):
        headers = {"Authorization": f"{get_auth_token()}"}

        resposta = requests.delete(
            url_produtos + f'/{self.produto["_id"]}', headers=headers)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["message"] == "Registro excluído com sucesso"

    def test_delete_produto_inexistente(self, faker, url_produtos, get_auth_token):
        headers = {"Authorization": f"{get_auth_token()}"}

        resposta = requests.delete(
            url_produtos + f'/{faker.uuid4()}', headers=headers)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["message"] == "Nenhum registro excluído"

    def test_delete_produto_contido_em_um_carrinho(self, get_auth_token, cadastrar_usuario, url_carrinhos, url_produtos):
        usuario = cadastrar_usuario()
        auth_token = get_auth_token(usuario['email'], usuario['password'])

        quantidade_produto = random.randint(1, 10)
        carrinho = Carrinho([ProdutoCarrinho(
            self.produto["_id"], quantidade_produto)])

        lista_de_produtos = []
        for item in carrinho.produtos:
            produto = {
                "idProduto": item.produto_id,
                "quantidade": item.quantidade
            }
            lista_de_produtos.append(produto)

        headers = {"Authorization": f"{auth_token}"}
        resposta = requests.post(url_carrinhos, json={
            "produtos": lista_de_produtos
        }, headers=headers)

        cadastrar_carrinho_resposta = resposta.json()

        assert resposta.status_code == 201

        resposta = requests.delete(
            url_produtos + f"/{self.produto['_id']}", headers=headers)

        resposta_de_erro = resposta.json()

        assert resposta.status_code == 400
        assert resposta_de_erro["message"] == "Não é permitido excluir produto que faz parte de carrinho"
        assert resposta_de_erro["idCarrinhos"][0] == cadastrar_carrinho_resposta["_id"]

    def test_editar_produto_com_token_invalido(self, faker, url_produtos):
        headers = {"Authorization": f"{faker.uuid4()}"}

        resposta = requests.delete(
            url_produtos + f'/{self.produto["_id"]}', headers=headers)

        resposta_de_erro = resposta.json()
        assert resposta.status_code == 401
        assert resposta_de_erro["message"] == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"

    @pytest.mark.usuario_comum
    def test_delete_produto_com_usuario_comum(self, url_login, url_produtos):
        resposta = requests.post(url_login, json={
            "email": self.usuario["email"],
            "password": self.usuario["password"]
        })

        resposta_de_sucesso = resposta.json()

        headers = {"Authorization": f"{resposta_de_sucesso['authorization']}"}

        resposta = requests.delete(
            url_produtos + f'/{self.produto["_id"]}', headers=headers)

        resposta_de_erro = resposta.json()
        assert resposta.status_code == 403
        assert resposta_de_erro["message"] == "Rota exclusiva para administradores"
