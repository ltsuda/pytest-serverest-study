import random

from faker import Faker
fake = Faker()


class Produto:
    """Classe para representar um produto.

    Atributos:
        preco: Preço do produto
    """

    def __init__(self, preco=random.randint(10, 30000)):
        """Inicializa os atributos necessários da classe

        Args:
            preco (int, optional): Preço do produto (aleátorio por padrão)
        """
        self.nome = fake.name()
        self.preco = preco
        self.descricao = fake.sentence()
        self.quantidade = random.randint(1, 1000)
