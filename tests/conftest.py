import pytest
from api.app import create_app  # IMPORTAR A FUNÇÃO, NÃO O OBJETO app

@pytest.fixture
def app():
    """
    Fixture que cria uma instância da aplicação Flask para testes
    """
    app = create_app()  # Usa create_app() para ter todos os Namespaces e configs
    app.config.update({
        "TESTING": True,      # ativa modo de teste
        "JWT_SECRET_KEY": "super-secret-key"  # garante compatibilidade JWT
    })

    with app.app_context():
        yield app

@pytest.fixture
def client(app):
    """
    Fixture que cria um client de testes para fazer requests à API
    """
    return app.test_client()
