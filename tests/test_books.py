import pytest

@pytest.mark.parametrize("endpoint", [
    "/api/v1/books/",
    "/api/v1/books/1",
    "/api/v1/books/search?title=Clean",
    "/api/v1/books/search?category=Travel",
    "/api/v1/books/top-rated",
    "/api/v1/books/price-range?min=10&max=20",
])
def test_books_endpoints(client, endpoint):
    """
    Testa os endpoints obrigatórios e opcionais de books
    """
    response = client.get(endpoint)
    assert response.status_code in [200, 404]  # 404 se não houver dados na DB
    if response.status_code == 200:
        assert isinstance(response.json, list) or isinstance(response.json, dict)


def test_book_search_with_filters(client):
    """
    Testa /api/v1/books/search com múltiplos filtros
    """
    response = client.get("/api/v1/books/search?category=Travel&min_price=10&max_price=20&rating=4")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert isinstance(response.json, list)
        for book in response.json:
            if "category" in book:
                assert book["category"] == "Travel"
            if "price" in book:
                assert 10 <= book["price"] <= 20
            if "rating" in book:
                assert book["rating"] >= 4


def test_books_stats(client):
    """
    Testa /api/v1/books/stats
    """
    response = client.get("/api/v1/books/stats")
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert "total_books" in response.json
    assert "avg_price" in response.json or "average_price" in response.json
