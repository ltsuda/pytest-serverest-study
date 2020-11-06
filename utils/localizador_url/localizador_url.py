class LocalizadorURL:
    """Classe utilitária para representar um localizador de URL.

    Atributos:
        ip: Endereço IP do servidor ServeRest
        port: Porta do servidor ServeRest
    """

    def __init__(self, ip, port):
        """Inicializa os atributos necessários da classe

        Args:
            ip (str): Endereço IP do servidor ServeRest
            port (str): Porta do servidor ServeRest
        """
        self.base_url = f'http://{ip}:{port}'

    def get_url_login(self):
        """Constrói a URL de login

        Returns:
            str: Endpoint de login
        """
        return f'{self.base_url}/login'

    def get_url_usuarios(self):
        """Constrói a URL de usuários

        Returns:
            str: Endpoint de usuários
        """
        return f'{self.base_url}/usuarios'

    def get_url_produtos(self):
        """Constrói a URL de produtos

        Returns:
            str: Endpoint de produtos
        """
        return f'{self.base_url}/produtos'

    def get_url_carrinhos(self):
        """Constrói a URL de carrinhos

        Returns:
            str: Endpoint de carrinhos
        """
        return f'{self.base_url}/carrinhos'
