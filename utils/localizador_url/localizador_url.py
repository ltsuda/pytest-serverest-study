class LocalizadorURL(object):
    """
    Initiates the base API url and returns each endpoint
    exising in the ServeRest API.
    """

    def __init__(self, ip, port):
        self.base_url = f'http://{ip}:{port}'

    def get_url_login(self):
        return f'{self.base_url}/login'

    def get_url_usuarios(self):
        return f'{self.base_url}/usuarios'

    def get_url_produtos(self):
        return f'{self.base_url}/produtos'

    def get_url_carrinhos(self):
        return f'{self.base_url}/carrinhos'
