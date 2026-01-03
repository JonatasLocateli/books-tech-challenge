def test_health_endpoint(client):
    """
    Testa o endpoint /api/v1/health
    """
    response = client.get("/api/v1/health/")
    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_login_success(client):
    """
    Testa login bem-sucedido no endpoint /api/v1/auth/login
    """
    response = client.post("/api/v1/auth/login", json={
        "username": "admin",
        "password": "admin123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json
    assert "refresh_token" in response.json


def test_login_failure(client):
    """
    Testa login falho no endpoint /api/v1/auth/login
    """
    response = client.post("/api/v1/auth/login", json={
        "username": "admin",
        "password": "wrong"
    })
    assert response.status_code == 401
    assert "msg" in response.json
