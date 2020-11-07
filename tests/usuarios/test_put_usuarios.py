from model import Usuario

from copy import copy
import requests
import pytest


class TestPUTUsuarios:
    """
    Suite de testes do endpoint /usuarios e método PUT
    """

    @pytest.fixture(autouse=True)
    def setup_usuario(self, request, cadastrar_usuario):
        if 'usuario_existente' in request.keywords:
            self.usuario_existente = cadastrar_usuario()
        else:
            self.usuario = Usuario()

    @pytest.mark.usuario_existente
    def test_editar_usuario(self, faker, url_usuarios):
        usuario_modificado = copy(self.usuario_existente)
        usuario_modificado["password"] = faker.uuid4()

        resposta = requests.put(
            url_usuarios + f'/{self.usuario_existente["_id"]}', json={
                "nome": usuario_modificado["nome"],
                "email": usuario_modificado["email"],
                "password": usuario_modificado["password"],
                "administrador": usuario_modificado["administrador"]
            })

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["message"] == "Registro alterado com sucesso"

        query = f'?_id={self.usuario_existente["_id"]}'
        resposta = requests.get(url_usuarios + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["usuarios"][0] == usuario_modificado

    def test_editar_usuario_com_id_nao_encontrado(self, faker, url_usuarios):
        usuario_id = faker.uuid4()

        resposta = requests.put(url_usuarios + f"/{usuario_id}", json={
            "nome": self.usuario.nome,
            "email": self.usuario.email,
            "password": self.usuario.password,
            "administrador": self.usuario.administrador
        })

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 201
        assert resposta_de_sucesso["message"] == "Cadastro realizado com sucesso"
        assert "_id" in resposta_de_sucesso

    @pytest.mark.usuario_existente
    def test_editar_usuario_com_email_ja_existente_e_id_nao_encontrado(self, faker, cadastrar_usuario, url_usuarios):
        usuario_modificado = copy(self.usuario_existente)
        usuario_modificado["password"] = faker.uuid4()
        usuario_modificado_id = faker.uuid4()

        resposta = requests.put(
            url_usuarios + f'/{usuario_modificado_id}', json={
                "nome": usuario_modificado["nome"],
                "email": usuario_modificado["email"],
                "password": usuario_modificado["password"],
                "administrador": usuario_modificado["administrador"]
            })

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 400
        assert resposta_de_sucesso["message"] == "Este email já está sendo usado"
