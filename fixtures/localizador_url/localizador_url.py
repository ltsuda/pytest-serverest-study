from utils import LocalizadorURL

import pytest


@pytest.fixture(scope='session')
def get_url_principal(variables):
    """Fixture que constrói um objeto LocalizadorURL e retorna o endereço base do servidor

        Args:
            variables (dict): Dicionário com configurações carregadas pelo plugin pytest-variables

        Returns:
            (str) = URL principal do servidor
    """
    return LocalizadorURL(
        variables['ip'],
        variables['port']
    )


@pytest.fixture(scope='module')
def url_login(get_url_principal):
    """Fixture que constrói o endpoint de login

        Args:
            get_url_principal (fixtures[str]): URL principal do servidor retornada pela fixture

        Returns:
            (str) = URL completa do endpoint de login
    """
    return get_url_principal.get_url_login()


@pytest.fixture(scope='module')
def url_usuarios(get_url_principal):
    """Fixture que constrói o endpoint de usuários

        Args:
            get_url_principal (fixtures[str]): URL principal do servidor retornada pela fixture

        Returns:
            (str) = URL completa do endpoint de usuários
    """
    return get_url_principal.get_url_usuarios()


@pytest.fixture(scope='module')
def url_produtos(get_url_principal):
    """Fixture que constrói o endpoint de produtos

        Args:
            get_url_principal (fixtures[str]): URL principal do servidor retornada pela fixture

        Returns:
            (str) = URL completa do endpoint de produtos
    """
    return get_url_principal.get_url_produtos()


@pytest.fixture(scope='module')
def url_carrinhos(get_url_principal):
    """Fixture que constrói o endpoint de carrinhos

        Args:
            get_url_principal (fixtures[str]): URL principal do servidor retornada pela fixture

        Returns:
            (str) = URL completa do endpoint de carrinhos
    """
    return get_url_principal.get_url_carrinhos()
