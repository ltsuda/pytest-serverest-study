![pytest](https://github.com/ltsuda/pytest-serverest-study/workflows/pytest/badge.svg) [![Badge ServeRest](https://img.shields.io/badge/API-ServeRest-green)](https://github.com/PauloGoncalvesBH/ServeRest/)

# Pytest API Study
Repositório utilizado como estudo de automação de testes de REST API utilizando Pytest


## Servidor REST API
Como neste projeto foi utilizado como estudo o servidor ServeRest, o mesmo é necessário para que os testes automatizados sejam executados.
> Para as instruções de como iniciar o servidor REST, siga a documentação do projeto [ServeRest](https://github.com/PauloGoncalvesBH/ServeRest#consumindo-o-serverest)

## Instalação e execução

### Pré requisitos

- [Git](https://git-scm.com/downloads)
- [Python 3.8+](https://www.python.org/downloads/)
  - Como alternativa, pode ser utilizado o gerenciador de versão Python [Pyenv](https://github.com/pyenv/pyenv) para a instalação do Python
- [Poetry](https://python-poetry.org/docs/)

#### Clonando reposiótorio

```text
git clone https://github.com/ltsuda/pytest-serverest-study.git
```

#### Instalando dependências Python
```text
> cd pytest-serverest-study
> poetry install # aguarde enquanto são instaladas as dependências
> poetry shell   # ativando ambiente virtual
pytest-serverest-study > poetry run pytest --variables config/config.json
```

Se tudo der certo, o resultado será apresentado conforme imagem abaixo:
![image](https://user-images.githubusercontent.com/3965277/99024258-f1d1e280-2544-11eb-9977-1e9553586879.png)

### Estrutura de diretórios
```text
.
├── __init__.py
├── config
│   └── config.json
├── fixtures
│   ├── __init__.py
│   └── rotas*/
│       ├── __init__.py
│       └── *.py
├── model
│   ├── __init__.py
│   └── modelos*/
│       ├── __init__.py
│       └── *.py

├── poetry.lock
├── pyproject.toml
├── pytest.ini
├── tests
│   ├── __init__.py
│   ├── rota*/
│   │   ├── __init__.py
│   │   ├── test_delete_rota*.py
│   │   ├── test_get_rota*.py
│   │   ├── test_post_rota*.py
│   │   └── test_put_rota*.py
│   └── conftest.py
└── utils
    ├── __init__.py
    └── localizador_url
        ├── __init__.py
        └── localizador_url.py
```

* [config/](https://github.com/ltsuda/pytest-serverest-study/tree/main/config): diretório com variáveis de ambiente. Exemplo: ip do servidor, email e senha do usuário padrão já existente no ServeRest
* [fixtures/](https://github.com/ltsuda/pytest-serverest-study/tree/main/fixtures)*: diretórios com métodos compartilhados ([Fixtures](https://docs.pytest.org/en/stable/fixture.html)) que podem ser facilmente acessados pelos testes, evitando duplicação de código
  * carrinhos/carrinhos.py: diretório e arquivo com fixtures relacionados ao endpoint de carrinhos
* [model/](https://github.com/ltsuda/pytest-serverest-study/tree/main/model)*: diretório com as classes modelo representando cada tipo objeto a ser enviado para o servidor
  * usuario/usuario.py: diretório e arquivo do modelo de usuário com nome, email, senha e propriedade administrador para indicar se o mesmo tem privilégios de administração
* [utils/](https://github.com/ltsuda/pytest-serverest-study/tree/main/utils): diretório com módulo auxiliar com metódos de contrução dos endpoints a serem testados
* [tests/](https://github.com/ltsuda/pytest-serverest-study/tree/main/tests)*: diretório com os testes das rotas e arquivo de configuração pytest para descoberta de fixtures
  * produtos/: diretório com testes da rota de produtos
    - test_delete_produtos.py Arquivo de teste do método DELETE
    - test_get_produtos.py    Arquivo de teste do método GET
    - test_post_produtos.py   Arquivo de teste do método POST
    - test_put_produtos.py    Arquivo de teste do método PUT
  * conftest.py Arquivo para importação e descoberta das fixtures
* [poetry.lock](https://github.com/ltsuda/pytest-serverest-study/blob/main/poetry.lock) [[doc]](https://python-poetry.org/docs/basic-usage/#installing-without-poetrylock): Arquivo com as informações das dependências do projeto
* [pyproject.toml](https://github.com/ltsuda/pytest-serverest-study/blob/main/pyproject.toml) [[doc]](https://python-poetry.org/docs/basic-usage/#project-setup): Arquivo com os requisitos, requisitos de desenvolvimento e metadata do **projeto**
* [pytest.ini](https://github.com/ltsuda/pytest-serverest-study/blob/main/pytest.ini) [[doc]](https://docs.pytest.org/en/stable/customize.html#pytest-ini): Arquivo de configuração do pytest, utilizado para criação de marcadores que podem ser utilizados ou não pelos testes, assim podendo indicar se o teste deve ter alguma configuração específica
