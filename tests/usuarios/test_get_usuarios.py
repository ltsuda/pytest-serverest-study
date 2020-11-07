import pytest
import requests


class TestGETUsuarios:
    """
    Suite de testes do endpoint /usuarios e método GET
    """

    @pytest.fixture(autouse=True)
    def setup_usuario(self, cadastrar_usuario):
        self.usuario = cadastrar_usuario()

    def test_buscar_usuarios(self, url_usuarios):
        resposta = requests.get(url_usuarios)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] > 1
        assert self.usuario in resposta_de_sucesso["usuarios"]

    def test_buscar_usuario_por_id(self, url_usuarios):
        query = f'?_id={self.usuario["_id"]}'
        resposta = requests.get(url_usuarios + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] == 1
        assert resposta_de_sucesso["usuarios"][0] == self.usuario

    def test_buscar_usuario_por_nome(self, url_usuarios):
        query = f'?nome={self.usuario["nome"]}'
        resposta = requests.get(url_usuarios + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] >= 1

        usuarios = resposta_de_sucesso["usuarios"]
        somente_nome_buscado = set([item["nome"] for item in usuarios])
        assert len(somente_nome_buscado) == 1
        assert somente_nome_buscado.pop() == self.usuario["nome"]

    def test_buscar_usuario_por_email(self, url_usuarios):
        query = f'?email={self.usuario["email"]}'
        resposta = requests.get(url_usuarios + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] == 1
        assert resposta_de_sucesso["usuarios"][0] == self.usuario

    def test_buscar_usuario_por_password(self, url_usuarios):
        query = f'?password={self.usuario["password"]}'
        resposta = requests.get(url_usuarios + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] >= 1

        usuarios = resposta_de_sucesso["usuarios"]
        somente_password_buscado = set([item["password"] for item in usuarios])
        assert len(somente_password_buscado) == 1
        assert somente_password_buscado.pop() == self.usuario["password"]

    def test_buscar_usuario_administrador(self, url_usuarios):
        query = f'?administrador={self.usuario["administrador"]}'
        resposta = requests.get(url_usuarios + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] >= 1

        usuarios = resposta_de_sucesso["usuarios"]
        somente_campo_administrador_buscado = set(
            [item["administrador"] for item in usuarios])
        assert len(somente_campo_administrador_buscado) == 1
        assert somente_campo_administrador_buscado.pop(
        ) == self.usuario["administrador"]

    def test_buscar_usuario_por_nome_e_administrador(self, url_usuarios):
        query = f'?nome={self.usuario["nome"]}&administrador={self.usuario["administrador"]}'
        resposta = requests.get(url_usuarios + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] >= 1

        usuarios = resposta_de_sucesso["usuarios"]
        somente_campo_administrador = set(
            [item["administrador"] for item in usuarios])
        somente_nome_buscado = set([item["nome"] for item in usuarios])
        assert len(somente_campo_administrador) and len(
            somente_nome_buscado) == 1
        assert somente_campo_administrador.pop(
        ) == self.usuario["administrador"]
        assert somente_nome_buscado.pop() == self.usuario["nome"]
