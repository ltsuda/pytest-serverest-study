import pytest
import requests


class TestLoginSchema:
    """
    Suite de testes do schema do endpoint /login
    """

    def test_login_schema(self, url_login, valida_schema):
        resposta = requests.post(url_login, json={})

        assert resposta.status_code == 400
        valida_schema(suite='login', data=resposta.json(),
                      filename='post_sem_dados')
