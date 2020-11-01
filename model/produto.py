import random

from faker import Faker
fake = Faker()


class Produto(object):
    """
    Classe que representa um produto.
    """

    def __init__(self, preco=random.randint(10, 30000)):
        self.nome = fake.company()
        self.preco = preco
        self.descricao = fake.sentence()
        self.quantidade = random.randint(1, 1000)
