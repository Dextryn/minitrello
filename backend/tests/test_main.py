import pytest

def test_create_user(client):
    payload = {
        "email": "testuser@email.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "password123"
    }

    response = client.post("/users/", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["email"] == payload["email"]
    assert data["first_name"] == payload["first_name"]
    assert data["last_name"] == payload["last_name"]
    assert "user_id" in data
    assert "created_at" in data
    assert "password" not in data
