from faker import Faker


class Usuario(object):
    """
    Representation of a user from the API server.
    """
    def __init__(self, administrator=''):
        self.name = fake.name()
        self.email = fake.email()
        self.password = fake.misc.password()
        self.administrator = True if administrator else fake.misc.boolean()
