from faker import Faker
fake = Faker()


class Usuario(object):
    """
    Representation of a user from the API server.
    """

    def __init__(self, administrador="false"):
        self.nome = fake.name()
        self.email = fake.email()
        self.password = fake.password(length=24)
        self.administrador = administrador
