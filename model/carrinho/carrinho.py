class ProdutoCarrinho(object):
    """
    Representa um produto contido em um carrinho.
    """

    def __init__(self, produto_id, quantidade=0):
        self.produto_id = produto_id
        self.quantidade = quantidade


class Carrinho(object):
    """
    Representa um carrinho de compras.
    """

    def __init__(self, produtos=[ProdutoCarrinho]):
        self.produtos = produtos
