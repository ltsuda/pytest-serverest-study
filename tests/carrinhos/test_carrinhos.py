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

    def test_cadastrar_carrinho(self, get_auth_token, cadastrar_usuario, cadastrar_produto, carrinhos_url):
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
        resposta = requests.post(carrinhos_url, json={
            "produtos": lista_de_produtos
        }, headers=headers)

        resposta_de_sucesso = resposta.json()

        assert resposta.status_code == 201
        assert resposta_de_sucesso["message"] == "Cadastro realizado com sucesso"
        assert "_id" in resposta_de_sucesso

    def test_cadastrar_carrinho_com_produto_duplicado(self, get_auth_token, cadastrar_usuario, cadastrar_produto, carrinhos_url):
        usuario = cadastrar_usuario(administrador="false")
        auth_token = get_auth_token(usuario['email'], usuario['password'])

        produto_cadastrado = cadastrar_produto()
        quantidade_produto = random.randint(1, 10)
        carrinho = Carrinho([ProdutoCarrinho(
            produto_cadastrado["_id"], quantidade_produto)])

        lista_de_produtos = []
        for item in carrinho.produtos:
            produto = {
                "idProduto": item.produto_id,
                "quantidade": item.quantidade
            }
            lista_de_produtos.append(produto)
            lista_de_produtos.append(produto)

        headers = {"Authorization": f"{auth_token}"}
        resposta = requests.post(carrinhos_url, json={
            "produtos": lista_de_produtos
        }, headers=headers)

        resposta_de_sucesso = resposta.json()

        assert resposta.status_code == 400
        assert resposta_de_sucesso["message"] == "Não é permitido possuir produto duplicado"
        assert produto_cadastrado["_id"] == resposta_de_sucesso["idProdutosDuplicados"][0]

    def test_cadastrar_mais_de_um_carrinho(self, get_auth_token, cadastrar_usuario, cadastrar_produto, carrinhos_url):
        usuario = cadastrar_usuario(administrador="false")
        auth_token = get_auth_token(usuario['email'], usuario['password'])

        produto_cadastrado = cadastrar_produto()
        quantidade_produto = random.randint(1, 10)
        carrinho = Carrinho([ProdutoCarrinho(
            produto_cadastrado["_id"], quantidade_produto)])

        lista_de_produtos = []
        for item in carrinho.produtos:
            produto = {
                "idProduto": item.produto_id,
                "quantidade": item.quantidade
            }
            lista_de_produtos.append(produto)

        headers = {"Authorization": f"{auth_token}"}
        resposta = requests.post(carrinhos_url, json={
            "produtos": lista_de_produtos
        }, headers=headers)
        assert resposta.status_code == 201

        resposta = requests.post(carrinhos_url, json={
            "produtos": lista_de_produtos
        }, headers=headers)

        resposta_de_sucesso = resposta.json()

        assert resposta.status_code == 400
        assert resposta_de_sucesso["message"] == "Não é permitido ter mais de 1 carrinho"

    def test_cadastrar_carrinho_produto_inexistente(self, faker, get_auth_token, cadastrar_usuario, cadastrar_produto, carrinhos_url):
        usuario = cadastrar_usuario(administrador="false")
        auth_token = get_auth_token(usuario['email'], usuario['password'])

        lista_de_produtos = []
        produto = {
            "idProduto": faker.uuid4(),
            "quantidade": random.randint(1, 10)
        }
        lista_de_produtos.append(produto)

        headers = {"Authorization": f"{auth_token}"}
        resposta = requests.post(carrinhos_url, json={
            "produtos": lista_de_produtos
        }, headers=headers)

        resposta_de_sucesso = resposta.json()

        assert resposta.status_code == 400
        assert resposta_de_sucesso["message"] == "Produto não encontrado"
        assert resposta_de_sucesso["item"]["idProduto"] == produto["idProduto"]
        assert resposta_de_sucesso["item"]["quantidade"] == produto["quantidade"]

    def test_cadastrar_carrinho_quantidade_produto_insuficiente(self, get_auth_token, cadastrar_usuario, cadastrar_produto, carrinhos_url):
        usuario = cadastrar_usuario(administrador="false")
        auth_token = get_auth_token(usuario['email'], usuario['password'])

        produto_cadastrado = cadastrar_produto()
        quantidade_produto = random.randint(1, 10)
        carrinho = Carrinho([ProdutoCarrinho(
            produto_cadastrado["_id"], quantidade_produto)])

        lista_de_produtos = []
        for item in carrinho.produtos:
            produto = {
                "idProduto": item.produto_id,
                "quantidade": 50000
            }
            lista_de_produtos.append(produto)

        headers = {"Authorization": f"{auth_token}"}
        resposta = requests.post(carrinhos_url, json={
            "produtos": lista_de_produtos
        }, headers=headers)

        resposta_de_sucesso = resposta.json()

        assert resposta.status_code == 400
        assert resposta_de_sucesso["message"] == "Produto não possui quantidade suficiente"
        assert resposta_de_sucesso["item"]["idProduto"] == produto_cadastrado["_id"]
        assert resposta_de_sucesso["item"]["quantidade"] == lista_de_produtos[0]["quantidade"]
        assert resposta_de_sucesso["item"]["quantidadeEstoque"] == produto_cadastrado["quantidade"]

    def test_cadastrar_carrinho_com_token_invalido(self, faker, get_auth_token, cadastrar_usuario, cadastrar_produto, carrinhos_url):
        usuario = cadastrar_usuario(administrador="false")

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

        headers = {"Authorization": f"{faker.uuid4()}"}
        resposta = requests.post(carrinhos_url, json={
            "produtos": lista_de_produtos
        }, headers=headers)

        resposta_de_sucesso = resposta.json()

        assert resposta.status_code == 401
        assert resposta_de_sucesso["message"] == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"
