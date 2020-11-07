from faker import Faker
fake = Faker()


class Usuario:
    """Classe para representar um usuário.

    Atributos:
        administrador: Indica se o usuário é administrador
    """

    def __init__(self, administrador="false"):
        """Inicializa os atributos necessários da classe

        Args:
            administrador (str, optional): Indica se o usuário é administrador ("false" por padrão)
        """
        self.nome = fake.name()
        self.email = fake.email()
        self.password = fake.uuid4()
        self.administrador = administrador
