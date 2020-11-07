from model import ProdutoCarrinho

import random
import requests
import pytest


class TestDELETECarrinhos:
    """
    Suite de testes do endpoint /carrinhos e método DELETE
    """

    @pytest.fixture(autouse=True)
    def setup_carrinho(self, request, get_auth_token, cadastrar_produto, cadastrar_carrinho, cadastrar_usuario):
        usuario = cadastrar_usuario(administrador="false")
        auth_token = get_auth_token(
            usuario['email'], usuario['password'])
        self.headers = {"Authorization": f"{auth_token}"}

        produto = cadastrar_produto()
        quantidade_produto = random.randint(1, 10)
        produto_carrinho = [ProdutoCarrinho(
            produto["_id"], quantidade_produto)]

        if 'carrinho_inexistente' in request.keywords:
            return
        else:
            cadastrar_carrinho(produto_carrinho, auth_token)

    def test_concluir_compra(self, url_carrinhos):
        resposta = requests.delete(
            url_carrinhos + "/concluir-compra", headers=self.headers)

        resposta_de_sucesso = resposta.json()

        assert resposta.status_code == 200
        assert resposta_de_sucesso["message"] == "Registro excluído com sucesso"

    @pytest.mark.carrinho_inexistente
    def test_concluir_compra_com_carrinho_inexistente(self, url_carrinhos):
        resposta = requests.delete(
            url_carrinhos + "/concluir-compra", headers=self.headers)

        resposta_de_sucesso = resposta.json()

        assert resposta.status_code == 200
        assert resposta_de_sucesso["message"] == "Não foi encontrado carrinho para esse usuário"

    def test_concluir_compra_com_token_invalido(self, faker, url_carrinhos):
        headers = {"Authorization": f"{faker.uuid4()}"}
        resposta = requests.delete(
            url_carrinhos + "/concluir-compra", headers=headers)

        resposta_de_erro = resposta.json()

        assert resposta.status_code == 401
        assert resposta_de_erro["message"] == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"

    def test_cancelar_compra(self, url_carrinhos):
        resposta = requests.delete(
            url_carrinhos + "/cancelar-compra", headers=self.headers)

        resposta_de_sucesso = resposta.json()

        assert resposta.status_code == 200
        assert resposta_de_sucesso["message"] == "Registro excluído com sucesso. Estoque dos produtos reabastecido"

    @pytest.mark.carrinho_inexistente
    def test_cancelar_compra_usuario_sem_carrinho(self, url_carrinhos):
        resposta = requests.delete(
            url_carrinhos + "/cancelar-compra", headers=self.headers)

        resposta_de_sucesso = resposta.json()

        assert resposta.status_code == 200
        assert resposta_de_sucesso["message"] == "Não foi encontrado carrinho para esse usuário"

    def test_cancelar_compra_com_token_invalido(self, faker, url_carrinhos):
        headers = {"Authorization": f"{faker.uuid4()}"}
        resposta = requests.delete(
            url_carrinhos + "/cancelar-compra", headers=headers)

        resposta_de_erro = resposta.json()

        assert resposta.status_code == 401
        assert resposta_de_erro["message"] == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"
