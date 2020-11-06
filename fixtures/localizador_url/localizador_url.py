from utils.localizador_url.localizador_url import LocalizadorURL

import pytest


@pytest.fixture(scope='session')
def get_url_principal(variables):
    return LocalizadorURL(
        variables['ip'],
        variables['port']
    )


@pytest.fixture(scope='module')
def url_login(get_url_principal):
    return get_url_principal.get_url_login()


@pytest.fixture(scope='module')
def url_usuarios(get_url_principal):
    return get_url_principal.get_url_usuarios()


@pytest.fixture(scope='module')
def url_produtos(get_url_principal):
    return get_url_principal.get_url_produtos()


@pytest.fixture(scope='module')
def url_carrinhos(get_url_principal):
    return get_url_principal.get_url_carrinhos()
