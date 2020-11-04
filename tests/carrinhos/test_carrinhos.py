from model.carrinho import ProdutoCarrinho, Carrinho
import random
import pytest
import requests


class TestCarrinhos:
    """
    Classe de testes do endpoint /produtos
    """

    def test_buscar_carrinhos(self, get_auth_token, cadastrar_usuario, cadastrar_produto, cadastrar_carrinho, carrinhos_url):
        usuario = cadastrar_usuario(administrador="false")
        auth_token = get_auth_token(usuario['email'], usuario['password'])

        produto = cadastrar_produto()
        quantidade_produto = random.randint(1, 10)
        produto_carrinho = [ProdutoCarrinho(
            produto["_id"], quantidade_produto)]
        carrinho = cadastrar_carrinho(produto_carrinho, auth_token)

        carrinho_esperado = {
            "produtos": [{
                "idProduto": produto["_id"],
                "quantidade": quantidade_produto,
                "precoUnitario": produto["preco"]
            }],
            "precoTotal": produto["preco"] * quantidade_produto,
            "quantidadeTotal": quantidade_produto,
            "idUsuario": usuario["_id"],
            "_id": carrinho["_id"]
        }

        resposta = requests.get(carrinhos_url)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] >= 1
        assert carrinho_esperado in resposta_de_sucesso["carrinhos"]

    def test_buscar_carrinho_por_id(self, get_auth_token, cadastrar_usuario, cadastrar_produto, cadastrar_carrinho, carrinhos_url):
        usuario = cadastrar_usuario(administrador="false")
        auth_token = get_auth_token(usuario['email'], usuario['password'])

        produto = cadastrar_produto()
        quantidade_produto = random.randint(1, 10)
        produto_carrinho = [ProdutoCarrinho(
            produto["_id"], quantidade_produto)]
        carrinho = cadastrar_carrinho(produto_carrinho, auth_token)

        carrinho_esperado = {
            "produtos": [{
                "idProduto": produto["_id"],
                "quantidade": quantidade_produto,
                "precoUnitario": produto["preco"]
            }],
            "precoTotal": produto["preco"] * quantidade_produto,
            "quantidadeTotal": quantidade_produto,
            "idUsuario": usuario["_id"],
            "_id": carrinho["_id"]
        }

        query = f'?_id={carrinho["_id"]}'
        resposta = requests.get(carrinhos_url + query)
        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] == 1
        assert carrinho_esperado == resposta_de_sucesso["carrinhos"][0]

    def test_buscar_carrinho_por_preco_total(self, get_auth_token, cadastrar_usuario, cadastrar_produto, cadastrar_carrinho, carrinhos_url):
        usuario = cadastrar_usuario(administrador="false")
        auth_token = get_auth_token(usuario['email'], usuario['password'])

        produto = cadastrar_produto()
        quantidade_produto = random.randint(1, 10)
        produto_carrinho = [ProdutoCarrinho(
            produto["_id"], quantidade_produto)]
        carrinho = cadastrar_carrinho(produto_carrinho, auth_token)

        carrinho_esperado = {
            "produtos": [{
                "idProduto": produto["_id"],
                "quantidade": quantidade_produto,
                "precoUnitario": produto["preco"]
            }],
            "precoTotal": produto["preco"] * quantidade_produto,
            "quantidadeTotal": quantidade_produto,
            "idUsuario": usuario["_id"],
            "_id": carrinho["_id"]
        }

        query = f'?precoTotal={carrinho_esperado["precoTotal"]}'
        resposta = requests.get(carrinhos_url + query)
        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] >= 1
        assert carrinho_esperado in resposta_de_sucesso["carrinhos"]

    def test_buscar_carrinho_por_preco_total(self, get_auth_token, cadastrar_usuario, cadastrar_produto, cadastrar_carrinho, carrinhos_url):
        usuario = cadastrar_usuario(administrador="false")
        auth_token = get_auth_token(usuario['email'], usuario['password'])

        produto = cadastrar_produto()
        quantidade_produto = random.randint(1, 10)
        produto_carrinho = [ProdutoCarrinho(
            produto["_id"], quantidade_produto)]
        carrinho = cadastrar_carrinho(produto_carrinho, auth_token)

        carrinho_esperado = {
            "produtos": [{
                "idProduto": produto["_id"],
                "quantidade": quantidade_produto,
                "precoUnitario": produto["preco"]
            }],
            "precoTotal": produto["preco"] * quantidade_produto,
            "quantidadeTotal": quantidade_produto,
            "idUsuario": usuario["_id"],
            "_id": carrinho["_id"]
        }

        query = f'?quantidadeTotal={carrinho_esperado["quantidadeTotal"]}'
        resposta = requests.get(carrinhos_url + query)
        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] >= 1
        assert carrinho_esperado in resposta_de_sucesso["carrinhos"]

    def test_buscar_carrinho_por_usuario_id(self, get_auth_token, cadastrar_usuario, cadastrar_produto, cadastrar_carrinho, carrinhos_url):
        usuario = cadastrar_usuario(administrador="false")
        auth_token = get_auth_token(usuario['email'], usuario['password'])

        produto = cadastrar_produto()
        quantidade_produto = random.randint(1, 10)
        produto_carrinho = [ProdutoCarrinho(
            produto["_id"], quantidade_produto)]
        carrinho = cadastrar_carrinho(produto_carrinho, auth_token)

        carrinho_esperado = {
            "produtos": [{
                "idProduto": produto["_id"],
                "quantidade": quantidade_produto,
                "precoUnitario": produto["preco"]
            }],
            "precoTotal": produto["preco"] * quantidade_produto,
            "quantidadeTotal": quantidade_produto,
            "idUsuario": usuario["_id"],
            "_id": carrinho["_id"]
        }

        query = f'?idUsuario={carrinho_esperado["idUsuario"]}'
        resposta = requests.get(carrinhos_url + query)
        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] == 1
        assert carrinho_esperado == resposta_de_sucesso["carrinhos"][0]

    def test_buscar_carrinho_por_quantidade_e_preco_total(self, get_auth_token, cadastrar_usuario, cadastrar_produto, cadastrar_carrinho, carrinhos_url):
        usuario = cadastrar_usuario(administrador="false")
        auth_token = get_auth_token(usuario['email'], usuario['password'])

        produto = cadastrar_produto()
        quantidade_produto = random.randint(1, 10)
        produto_carrinho = [ProdutoCarrinho(
            produto["_id"], quantidade_produto)]
        carrinho = cadastrar_carrinho(produto_carrinho, auth_token)

        carrinho_esperado = {
            "produtos": [{
                "idProduto": produto["_id"],
                "quantidade": quantidade_produto,
                "precoUnitario": produto["preco"]
            }],
            "precoTotal": produto["preco"] * quantidade_produto,
            "quantidadeTotal": quantidade_produto,
            "idUsuario": usuario["_id"],
            "_id": carrinho["_id"]
        }

        query = f'?quantidadeTotal={carrinho_esperado["quantidadeTotal"]}&precoTotal={carrinho_esperado["precoTotal"]}'
        resposta = requests.get(carrinhos_url + query)
        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] == 1
        assert carrinho_esperado == resposta_de_sucesso["carrinhos"][0]
