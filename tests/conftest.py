import pytest

from fixtures.login.login import get_auth_token
from fixtures.usuario.usuario import cadastrar_usuario
from fixtures.produto.produto import cadastrar_produto
from fixtures.carrinho.carrinho import cadastrar_carrinho
from fixtures.localizador_url.localizador_url import get_url_principal, url_login , url_carrinhos, url_produtos, url_usuarios, url_usuarios