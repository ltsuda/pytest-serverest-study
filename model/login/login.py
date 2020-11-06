class Login:
    """Classe para representar o login do sistema.

    Atributos:
        email: Endereço de email do usuário
        password: Senha do usuário
    """

    def __init__(self, email, password):
        """Inicializa os atributos necessários da classe

        Args:
            email (str): Endereço de email do usuário
            password (str): Senha do usuário
        """
        self.email = email
        self.password = password
