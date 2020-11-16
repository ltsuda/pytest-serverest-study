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

    def test_login_com_administrador(self, url_login, valida_schema):
        resposta = requests.post(url_login, json={
            "email": self.usuario["email"],
            "password": self.usuario["password"]
        })

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        valida_schema(suite='login', data=resposta_de_sucesso,
                      filename='post')
        assert resposta_de_sucesso["message"] == "Login realizado com sucesso"

    @pytest.mark.usuario_comum
    def test_login_com_usuario_comum(self, url_login, valida_schema):
        resposta = requests.post(url_login, json={
            "email": self.usuario["email"],
            "password": self.usuario["password"]
        })

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        valida_schema(suite='login', data=resposta_de_sucesso,
                      filename='post')
        assert resposta_de_sucesso["message"] == "Login realizado com sucesso"

    def test_login_com_email_invalido(self, url_login, valida_schema):
        resposta = requests.post(url_login, json={
            "email": "invalid@gmail.com",
            "password": self.usuario["password"]
        })

        resposta_com_erro = resposta.json()
        assert resposta.status_code == 401
        valida_schema(suite='login', data=resposta_com_erro,
                      filename='post_dados_invalidos')
        assert resposta_com_erro["message"] == "Email e/ou senha inválidos"

    def test_login_com_senha_invalida(self, url_login, valida_schema):
        resposta = requests.post(url_login, json={
            "email": self.usuario["email"],
            "password": "invalid"
        })

        resposta_com_erro = resposta.json()
        assert resposta.status_code == 401
        valida_schema(suite='login', data=resposta_com_erro,
                      filename='post_dados_invalidos')
        assert resposta_com_erro["message"] == "Email e/ou senha inválidos"
