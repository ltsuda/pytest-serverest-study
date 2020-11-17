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
