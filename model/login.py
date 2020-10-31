class Login(object):
    """
    Represents the login model used to authenticate with API.
    """
    def __init__(self, email, password):
        self.email = email
        self.password = password
