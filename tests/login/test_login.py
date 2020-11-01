import pytest
import requests


class TestLogin:
    """
    TestLogin that holds the valid login tests.
    """

    def test_admin(self, cadastrar_usuario, login_url):
        usuario = cadastrar_usuario()
        response = requests.post(login_url, json={
            "email": usuario["email"],
            "password": usuario["password"]
        })

        success_response = response.json()
        assert success_response["message"] == "Login realizado com sucesso"
        assert "authorization" in success_response
        assert "Bearer" in success_response["authorization"]

    def test_non_admin(self, cadastrar_usuario, login_url):
        usuario = cadastrar_usuario(administrador="false")
        response = requests.post(login_url, json={
            "email": usuario["email"],
            "password": usuario["password"]
        })

        success_response = response.json()
        assert response.status_code == 200
        assert success_response["message"] == "Login realizado com sucesso"
        assert "authorization" in success_response
        assert "Bearer" in success_response["authorization"]

    def test_invalid_email(self, cadastrar_usuario, login_url):
        usuario = cadastrar_usuario()
        response = requests.post(login_url, json={
            "email": "invalid@gmail.com",
            "password": usuario["password"]
        })

        error_response = response.json()
        assert response.status_code == 401
        assert error_response["message"] == "Email e/ou senha inválidos"

    def test_invalid_password(self, cadastrar_usuario, login_url):
        usuario = cadastrar_usuario()
        response = requests.post(login_url, json={
            "email": usuario["email"],
            "password": "invalid"
        })

        error_response = response.json()
        assert response.status_code == 401
        assert error_response["message"] == "Email e/ou senha inválidos"
