class URLLocator(object):
    """
    Initiates the base API url and returns each endpoint
    exising in the ServeRest API.
    """

    def __init__(self, ip, port):
        self.base_url = f'https://{ip}:{port}'

    def get_login_url(self):
        return f'{self.base_url}/login'

    def get_usuario_url(self):
        return f'{self.base_url}/usuarios'

    def get_produtos_url(self):
        return f'{self.base_url}/produtos'

    def get_carrinhos_url(self):
        return f'{self.base_url}/carrinhos'
