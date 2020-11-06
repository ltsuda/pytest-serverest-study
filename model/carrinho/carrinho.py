class ProdutoCarrinho:
    """Classe para representar um produto a ser adicionado a um carrinho.

    Atributos:
        produto_id: ID do produto cadastrado no servidor
        quantidade: Quantidade de produtos
    """

    def __init__(self, produto_id, quantidade=0):
        """Inicializa os atributos necessários da classe

        Args:
            produto_id (str): ID do produto cadastrado no servidor
            quantidade (int): Quantidade de produtos
        """
        self.produto_id = produto_id
        self.quantidade = quantidade


class Carrinho:
    """Classe para representar um carrinho de produtos.

    Atributos:
        produtos: Lista de produtos adicionados no carrinho
    """

    def __init__(self, produtos=[ProdutoCarrinho]):
        """Inicializa os atributos necessários da classe

        Args:
            produtos (list[ProdutoCarrinho]): Lista de produtos do tipo ProdutoCarrinho
        """
        self.produtos = produtos
