from jsonschema import validate

import json
import os
import pytest


@pytest.fixture(scope='module')
def valida_schema():
    """Fixture que retorna se o schema especificado está valido


    """
    def _valida(suite, data, filename):
        """Valida se os dados retornados pela API está em conformidade com o schema

        Args:
            suite (str): nome do suite de teste
            data (dict[json]): dados a serem validados
            filename (str): nome do arquivo do schema
        """

        schema_path = os.getcwd() + f"/schemas/{suite}/{filename}.json"
        with open(schema_path, 'r') as file:
            schema = json.load(file)

        return validate(instance=data, schema=schema)

    return _valida
