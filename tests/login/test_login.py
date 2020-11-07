import pytest
import requests


class TestLogin:
    """
    Suite de testes do endpoint /login
    """

    @pytest.fixture(autouse=True)
    def setup_usuario(self, request, cadastrar_usuario):
        if 'usuario_comum' in request.keywords:
            self.usuario = cadastrar_usuario(administrador="false")
        else:
            self.usuario = cadastrar_usuario()

    def test_login_com_administrador(self, url_login):
        resposta = requests.post(url_login, json={
            "email": self.usuario["email"],
            "password": self.usuario["password"]
        })

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["message"] == "Login realizado com sucesso"
        assert "authorization" in resposta_de_sucesso
        assert "Bearer" in resposta_de_sucesso["authorization"]

    @pytest.mark.usuario_comum
    def test_login_com_usuario_comum(self, url_login):
        resposta = requests.post(url_login, json={
            "email": self.usuario["email"],
            "password": self.usuario["password"]
        })

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["message"] == "Login realizado com sucesso"
        assert "authorization" in resposta_de_sucesso
        assert "Bearer" in resposta_de_sucesso["authorization"]

    def test_login_com_email_invalido(self, url_login):
        resposta = requests.post(url_login, json={
            "email": "invalid@gmail.com",
            "password": self.usuario["password"]
        })

        resposta_com_erro = resposta.json()
        assert resposta.status_code == 401
        assert resposta_com_erro["message"] == "Email e/ou senha inválidos"

    def test_login_com_senha_invalida(self, url_login):
        resposta = requests.post(url_login, json={
            "email": self.usuario["email"],
            "password": "invalid"
        })

        resposta_com_erro = resposta.json()
        assert resposta.status_code == 401
        assert resposta_com_erro["message"] == "Email e/ou senha inválidos"
