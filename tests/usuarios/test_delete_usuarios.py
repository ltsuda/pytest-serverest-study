from model import Usuario, ProdutoCarrinho, Carrinho

import requests
import random
import pytest


class TestDELETEUsuarios:
    """
    Suite de testes do endpoint /usuarios e método DELETE
    """

    @pytest.fixture(autouse=True)
    def setup_usuario(self, request, cadastrar_usuario):
        if 'usuario_comum' in request.keywords:
            self.usuario = cadastrar_usuario(administrador="false")
        else:
            self.usuario = cadastrar_usuario()

    def test_delete_usuario(self, url_usuarios):
        resposta = requests.delete(url_usuarios + f'/{self.usuario["_id"]}')

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["message"] == "Registro excluído com sucesso"

    def test_delete_usuario_inexistente(self, faker, url_usuarios):
        resposta = requests.delete(url_usuarios + f'/{faker.uuid4()}')

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["message"] == "Nenhum registro excluído"

    @pytest.mark.usuario_comum
    def test_delete_usuario_com_carrinho(self, get_auth_token, cadastrar_produto, url_carrinhos, url_usuarios):
        auth_token = get_auth_token(
            self.usuario['email'], self.usuario['password'])

        produto = cadastrar_produto()
        quantidade_produto = random.randint(1, 10)
        carrinho = Carrinho([ProdutoCarrinho(
            produto["_id"], quantidade_produto)])

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
            url_usuarios + f"/{self.usuario['_id']}", headers=headers)

        resposta_de_sucesso = resposta.json()

        assert resposta.status_code == 400
        assert resposta_de_sucesso["message"] == "Não é permitido excluir usuário com carrinho cadastrado"
        assert resposta_de_sucesso["idCarrinho"] == cadastrar_carrinho_resposta["_id"]
