import pytest

from fixtures.login.login import get_auth_token
from fixtures.usuario.usuario import cadastrar_usuario
from fixtures.produto.produto import cadastrar_produto
from fixtures.carrinho.carrinho import cadastrar_carrinho
from fixtures.localizador_url.localizador_url import get_base_url_locator, login_url,\
    usuarios_url, produtos_url, carrinhos_url
