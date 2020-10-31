import pytest

class TestClass:
    """
    TestClass that holds the valid login tests.
    """

    def setup_method(self, cadastrar_usuario):
        self.usuario = cadastrar_usuario

    def test_admin(self):
        print(self.usuario)
