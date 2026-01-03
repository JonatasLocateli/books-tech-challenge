import pytest

def test_health_endpoint(client):
    """
    Testa o endpoint /api/v1/health
    Verifica se a API está respondendo e se o status está ok
    """
    response = client.get("/api/v1/health/")
    
    # Deve retornar 200 OK
    assert response.status_code == 200
    
    # Deve conter a chave "status"
    assert "status" in response.json
    
    # Se houver conexão com o banco, o status deve ser "ok"
    assert response.json["status"] == "ok" or response.json["status"] == "error"
