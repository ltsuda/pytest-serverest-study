import pytest
import requests


class TestGETProdutos:
    """
    Suite de testes do endpoint /produtos e método GET
    """

    @pytest.fixture(autouse=True)
    def setup_produto(self, cadastrar_produto):
        self.produto = cadastrar_produto()

    def test_buscar_produtos(self, url_produtos):
        resposta = requests.get(url_produtos)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] > 1
        assert self.produto in resposta_de_sucesso["produtos"]

    def test_buscar_produto_por_id(self, url_produtos):
        query = f'?_id={self.produto["_id"]}'
        resposta = requests.get(url_produtos + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] == 1
        assert resposta_de_sucesso["produtos"][0] == self.produto

    def test_buscar_produto_por_nome(self, url_produtos):
        query = f'?nome={self.produto["nome"]}'
        resposta = requests.get(url_produtos + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] == 1
        assert resposta_de_sucesso["produtos"][0] == self.produto

    def test_buscar_produto_por_preco(self, url_produtos):
        query = f'?preco={self.produto["preco"]}'
        resposta = requests.get(url_produtos + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] >= 1

        produtos = resposta_de_sucesso["produtos"]
        somente_preco_buscado = set([item["preco"] for item in produtos])
        assert len(somente_preco_buscado) == 1
        assert somente_preco_buscado.pop() == self.produto["preco"]

    def test_buscar_produto_por_descricao(self, url_produtos):
        query = f'?descricao={self.produto["descricao"]}'
        resposta = requests.get(url_produtos + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] >= 1

        produtos = resposta_de_sucesso["produtos"]
        somente_descricao_buscada = set(
            [item["descricao"] for item in produtos])
        assert len(somente_descricao_buscada) == 1
        assert somente_descricao_buscada.pop() == self.produto["descricao"]

    def test_buscar_produto_por_quantidade(self, url_produtos):
        query = f'?quantidade={self.produto["quantidade"]}'
        resposta = requests.get(url_produtos + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] >= 1

        produtos = resposta_de_sucesso["produtos"]
        somente_quantidade_buscada = set(
            [item["quantidade"] for item in produtos])
        assert len(somente_quantidade_buscada) == 1
        assert somente_quantidade_buscada.pop() == self.produto["quantidade"]

    def test_buscar_produto_por_descricao_e_preco(self, url_produtos):
        query = f'?descricao={self.produto["descricao"]}&preco={self.produto["preco"]}'
        resposta = requests.get(url_produtos + query)

        resposta_de_sucesso = resposta.json()
        assert resposta.status_code == 200
        assert resposta_de_sucesso["quantidade"] >= 1

        produtos = resposta_de_sucesso["produtos"]
        somente_preco_buscado = set(
            [item["preco"] for item in produtos])
        somente_descricao_buscada = set(
            [item["descricao"] for item in produtos])
        assert len(somente_preco_buscado) and len(
            somente_descricao_buscada) == 1
        assert somente_preco_buscado.pop() == self.produto["preco"]
        assert somente_descricao_buscada.pop() == self.produto["descricao"]
