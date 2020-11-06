from model import Usuario
from model import ProdutoCarrinho, Carrinho

import pytest
import random
import requests
from copy import copy


class TestUsuarios:
    """
    Classe de testes do endpoint /usuarios
    """

    def test_buscar_usuarios(self, cadastrar_usuario, url_usuarios):
        usuario = cadastrar_usuario()
        resposta = requests.get(url_usuarios)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] > 1
        assert usuario in resposta_de_sucesso["usuarios"]

    def test_buscar_usuario_por_id(self, cadastrar_usuario, url_usuarios):
        usuario = cadastrar_usuario()

        query = f'?_id={usuario["_id"]}'
        resposta = requests.get(url_usuarios + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] == 1
        assert resposta_de_sucesso["usuarios"][0] == usuario

    def test_buscar_usuario_por_nome(self, cadastrar_usuario, url_usuarios):
        usuario = cadastrar_usuario()

        query = f'?nome={usuario["nome"]}'
        resposta = requests.get(url_usuarios + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] >= 1

        usuarios = resposta_de_sucesso["usuarios"]
        somente_nome_buscado = set([item["nome"] for item in usuarios])
        assert len(somente_nome_buscado) == 1
        assert somente_nome_buscado.pop() == usuario["nome"]

    def test_buscar_usuario_por_email(self, cadastrar_usuario, url_usuarios):
        usuario = cadastrar_usuario()

        query = f'?email={usuario["email"]}'
        resposta = requests.get(url_usuarios + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] == 1
        assert resposta_de_sucesso["usuarios"][0] == usuario

    def test_buscar_usuario_por_password(self, url_usuarios):
        usuario = Usuario()

        resposta = requests.post(url_usuarios, json={
            "nome": usuario.nome,
            "email": usuario.email,
            "password": "teste",
            "administrador": usuario.administrador
        })

        query = f'?password=teste'
        resposta = requests.get(url_usuarios + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] >= 1

        usuarios = resposta_de_sucesso["usuarios"]
        somente_password_buscado = set([item["password"] for item in usuarios])
        assert len(somente_password_buscado) == 1
        assert somente_password_buscado.pop() == "teste"

    def test_buscar_usuario_administrador(self, cadastrar_usuario, url_usuarios):
        usuario = cadastrar_usuario()

        query = f'?administrador={usuario["administrador"]}'
        resposta = requests.get(url_usuarios + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] >= 1

        usuarios = resposta_de_sucesso["usuarios"]
        somente_campo_administrador_buscado = set(
            [item["administrador"] for item in usuarios])
        assert len(somente_campo_administrador_buscado) == 1
        assert somente_campo_administrador_buscado.pop(
        ) == usuario["administrador"]

    def test_buscar_usuario_por_nome_e_admin(self, cadastrar_usuario, url_usuarios):
        usuario = cadastrar_usuario()

        query = f'?nome={usuario["nome"]}&administrador={usuario["administrador"]}'
        resposta = requests.get(url_usuarios + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] >= 1

        usuarios = resposta_de_sucesso["usuarios"]
        somente_campo_administrador = set(
            [item["administrador"] for item in usuarios])
        somente_nome_buscado = set([item["nome"] for item in usuarios])
        assert len(somente_campo_administrador) == 1
        assert len(somente_nome_buscado) == 1
        assert somente_campo_administrador.pop() == usuario["administrador"]
        assert somente_nome_buscado.pop() == usuario["nome"]

    def test_cadastrar_usuario(self, url_usuarios):
        usuario = Usuario()

        resposta = requests.post(url_usuarios, json={
            "nome": usuario.nome,
            "email": usuario.email,
            "password": usuario.password,
            "administrador": usuario.administrador
        })

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 201
        assert resposta_de_sucesso["message"] == "Cadastro realizado com sucesso"
        assert "_id" in resposta_de_sucesso

    def test_cadastrar_usuario_existente(self, faker, cadastrar_usuario, url_usuarios):
        usuario = cadastrar_usuario()

        resposta = requests.post(
            url_usuarios, json={
                "nome": faker.name(),
                "email": usuario["email"],
                "password": faker.password(length=24),
                "administrador": random.choice(["true", "false"])
            })
        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 400
        assert resposta_de_sucesso["message"] == "Este email já está sendo usado"

    def test_editar_usuario(self, faker, cadastrar_usuario, url_usuarios):
        usuario = cadastrar_usuario()
        usuario_modificado = copy(usuario)
        usuario_modificado["password"] = faker.password(length=24)

        resposta = requests.put(
            url_usuarios + f'/{usuario["_id"]}', json={
                "nome": usuario_modificado["nome"],
                "email": usuario_modificado["email"],
                "password": usuario_modificado["password"],
                "administrador": usuario_modificado["administrador"]
            })

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["message"] == "Registro alterado com sucesso"

        query = f'?_id={usuario["_id"]}'
        resposta = requests.get(url_usuarios + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["usuarios"][0] == usuario_modificado

    def test_editar_criando_usuario(self, faker, url_usuarios):
        usuario = Usuario()
        usuario_id = faker.uuid4()

        resposta = requests.put(url_usuarios + f"/{usuario_id}", json={
            "nome": usuario.nome,
            "email": usuario.email,
            "password": usuario.password,
            "administrador": usuario.administrador
        })

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 201
        assert resposta_de_sucesso["message"] == "Cadastro realizado com sucesso"
        assert "_id" in resposta_de_sucesso

    def test_editar_criando_usuario_email_existente(self, faker, cadastrar_usuario, url_usuarios):
        usuario = cadastrar_usuario()
        usuario_modificado = copy(usuario)
        usuario_modificado["password"] = faker.password(length=24)
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

    def test_delete_usuario(self, cadastrar_usuario, url_usuarios):
        usuario = cadastrar_usuario()

        resposta = requests.delete(url_usuarios + f'/{usuario["_id"]}')

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["message"] == "Registro excluído com sucesso"

    def test_delete_usuario_inexistente(self, faker, url_usuarios):
        resposta = requests.delete(url_usuarios + f'/{faker.uuid4()}')

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["message"] == "Nenhum registro excluído"

    def test_delete_usuario_com_carrinho(self, get_auth_token, cadastrar_usuario, cadastrar_produto, url_carrinhos, url_usuarios):
        usuario = cadastrar_usuario(administrador="false")
        auth_token = get_auth_token(usuario['email'], usuario['password'])

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
            url_usuarios + f"/{usuario['_id']}", headers=headers)

        resposta_de_sucesso = resposta.json()

        assert resposta.status_code == 400
        assert resposta_de_sucesso["message"] == "Não é permitido excluir usuário com carrinho cadastrado"
        assert resposta_de_sucesso["idCarrinho"] == cadastrar_carrinho_resposta["_id"]
