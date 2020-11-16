import pytest
import requests


class TestLoginSchema:
    """
    Suite de testes do schema do endpoint /login
    """

    @pytest.fixture(autouse=True)
    def setup_usuario(self, cadastrar_usuario):
        self.usuario = cadastrar_usuario()

    def test_login_schema(self, url_login, valida_schema):

        user = {
            "email": self.usuario["email"],
            "password": self.usuario["password"]
        }

        resposta = requests.post(url_login, json=user)

        assert resposta.status_code == 200
        valida_schema(suite='login', data=resposta.json(),
                      filename='post')
