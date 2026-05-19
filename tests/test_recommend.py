from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)


def test_get_homepage_form():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Система рекомендаций книг" in response.text
    assert "ID Пользователя:" in response.text
    assert 'button type="submit"' in response.text


def test_get_recommendations_success():
    response = client.get("/?user_id=6&top_n=5")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

    assert "Результаты для Пользователя 6" in response.text or "Рекомендации для Пользователя 6" in response.text
    assert "<ol>" in response.text
    assert "<li>" in response.text


def test_get_recommendations_validation():
    response = client.get("/?user_id=not-a-number")
    assert response.status_code == 422
