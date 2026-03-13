import pytest

def test_create_user(client):
    payload = {
        "email": "testuser@email.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "password123"
    }

    response = client.post("/users/", json=payload)
    assert response.status_code == 201

    data = response.json()

    assert data["email"] == payload["email"]
    assert data["first_name"] == payload["first_name"]
    assert data["last_name"] == payload["last_name"]
    assert "user_id" in data
    assert "created_at" in data
    assert "password" not in data

def test_create_user_duplicate_email(client):
    payload = {
        "email": "duplicateuser@email.com",
        "first_name": "Duplicate",
        "last_name": "User",
        "password": "password123"
    }

    response = client.post("/users/", json=payload)
    assert response.status_code == 201

    response_dup = client.post("/users/", json=payload)

    assert response_dup.status_code == 400
    assert "already exists" in response_dup.json().get("detail", "").lower()

def test_get_user_by_id(client):
    payload = {
        "email": "getbyid@email.com",
        "first_name": "GetBy",
        "last_name": "ID",
        "password": "password123"
    }

    create_response = client.post("/users/", json=payload)
    assert create_response.status_code == 201

    created_user = create_response.json()
    user_id = created_user["user_id"]

    get_user = client.get(f"/users/{user_id}")
    assert get_user.status_code == 200

    validate_user = get_user.json()

    assert validate_user["user_id"] == user_id
    assert validate_user["email"] == payload["email"]
    assert validate_user["first_name"] == payload["first_name"]
    assert validate_user["last_name"] == payload["last_name"]

def test_get_user_not_found(client):
    non_existent_user_id = 9999999

    response = client.get(f"/users/{non_existent_user_id}")

    assert response.status_code == 404
    assert "not found" in response.json().get("detail", "").lower()

def test_update_user(client):
    payload = {
        "email": "updateuser@email.com",
        "first_name": "Original",
        "last_name": "Name",
        "password": "password123"
    }

    create_response = client.post("/users/", json=payload)
    assert create_response.status_code == 201

    user_id = create_response.json()["user_id"]

    update_payload = {
        "first_name": "Update",
        "last_name": "User"
    }

    update_response = client.put(f"/users/{user_id}", json=update_payload)
    assert update_response.status_code == 200

    updated_user = update_response.json()
    assert updated_user["first_name"] == "Update"
    assert updated_user["last_name"] == "User"
    assert updated_user["user_id"] == user_id

def test_delete_user(client):
    payload = {
        "email": "deleteuser@email.com",
        "first_name": "Delete",
        "last_name": "User",
        "password": "password123"
    }

    create_response = client.post("/users/", json=payload)
    assert create_response.status_code == 201

    user_id = create_response.json()["user_id"]

    delete_response = client.delete(f"/users/{user_id}")
    assert delete_response.status_code in (200, 204)

    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 404
