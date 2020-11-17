import pytest
import requests


class TestUsuariosSchema:
    """
    Suite de testes do schema do endpoint /usuarios
    """

    @pytest.fixture(autouse=True)
    def setup_usuario(self, cadastrar_usuario):
        self.usuario = cadastrar_usuario()

    def test_buscar_usuarios_schema(self, url_usuarios, valida_schema):
        resposta = requests.get(url_usuarios)

        assert resposta.status_code == 200
        valida_schema(suite='usuarios', data=resposta.json(),
                      filename='get')

    def test_criar_usuario_schema(self, faker, url_usuarios, valida_schema):
        resposta = requests.post(url_usuarios, json={})

        assert resposta.status_code == 400
        valida_schema(suite='usuarios', data=resposta.json(),
                      filename='post_sem_dados')
