from faker import Faker
fake = Faker()

class Usuario(object):
    """
    Representation of a user from the API server.
    """
    def __init__(self, administrator="false"):
        self.name = fake.name()
        self.email = fake.email()
        self.password = 'test'
        self.administrator = administrator
