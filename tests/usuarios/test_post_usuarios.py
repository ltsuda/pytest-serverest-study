from model import Usuario

import requests
import random
import pytest


class TestPOSTUsuarios:
    """
    Suite de testes do endpoint /usuarios e método POST
    """

    @pytest.fixture(autouse=True)
    def setup_usuario(self, request, cadastrar_usuario):
        if 'usuario_existente' in request.keywords:
            self.usuario_existente = cadastrar_usuario()
        else:
            self.usuario = Usuario()

    def test_cadastrar_usuario(self, url_usuarios, valida_schema):
        resposta = requests.post(url_usuarios, json={
            "nome": self.usuario.nome,
            "email": self.usuario.email,
            "password": self.usuario.password,
            "administrador": self.usuario.administrador
        })

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 201
        valida_schema(suite='usuarios', data=resposta_de_sucesso,
                      filename='post')
        assert resposta_de_sucesso["message"] == "Cadastro realizado com sucesso"

    @pytest.mark.usuario_existente
    def test_cadastrar_usuario_ja_existente(self, faker, url_usuarios, valida_schema):
        resposta = requests.post(
            url_usuarios, json={
                "nome": faker.name(),
                "email": self.usuario_existente["email"],
                "password": faker.uuid4(),
                "administrador": random.choice(["true", "false"])
            })
        resposta_de_erro = resposta.json()
        assert resposta.status_code == 400
        valida_schema(suite='usuarios', data=resposta_de_erro,
                      filename='post_já_existente')
        assert resposta_de_erro["message"] == "Este email já está sendo usado"
