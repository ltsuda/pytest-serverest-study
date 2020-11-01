import pytest

from fixtures.login import get_auth_token
from fixtures.usuario import cadastrar_usuario
from fixtures.produto import cadastrar_produto
from fixtures.url_locator import get_base_url_locator, login_url,\
    usuarios_url, produtos_url, carrinhos_url
