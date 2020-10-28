from api.fixtures.url_locator import get_url_locator
from ..utils.url_locator import URLLocator

import pytest


@pytest.fixture(scope='session'):
def get_base_url_locator(variables):
    return URLLocator(
        variables['ip'],
        variables['port']
    )


@pytest.fixture(scope='module'):
def login_url(get_base_url_locator):
    return get_base_url_locator.get_login_url()


@pytest.fixture(scope='module'):
def usuarios_url(get_base_url_locator):
    return get_base_url_locator.get_usuarios_url()


@pytest.fixture(scope='module'):
def produtos_url(get_base_url_locator):
    return get_base_url_locator.get_produtos_url()


@pytest.fixture(scope='module'):
def carrinhos_url(get_base_url_locator):
    return get_base_url_locator.get_carrinhos_url()
