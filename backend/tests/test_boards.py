import pytest

def test_create_board(client):
    payload = {
        "title": "Create Board",
        "description": "This is the first Board I am creating using API Call"
    }

    response = client.post("/boards/", json=payload)
    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert "board_id" in data
    assert "created_at" in data
    assert "updated_at" in data

def test_get_board_by_id(client):
    payload = {
        "title": "Get board by ID",
        "description": "Pulling this board by it's Board ID"
    }

    create_response = client.post("/boards/", json=payload)
    assert create_response.status_code == 201

    created_board = create_response.json()
    board_id = created_board["board_id"]

    get_board = client.get(f"/boards/{board_id}")

    validate_board = get_board.json()

    assert validate_board["board_id"] == board_id
    assert validate_board["title"] == payload["title"]
    assert validate_board["description"] == payload["description"]

def test_get_board_by_user_id(client):
    payload = {
        "title": "Get board by user_id",
        "description": "Pulling this board by it's user_id"
    }

    create_response = client.post("/boards/", json=payload)
    assert create_response.status_code == 201

    created_board = create_response.json()
    user_id = created_board["user_id"]

    get_response = client.get(f"/boards/user/{user_id}")
    assert get_response.status_code == 200

    validate_boards = get_response.json()

    validate_board = next(b for b in validate_boards if b["title"] == payload["title"])

    assert validate_board["user_id"] == user_id
    assert validate_board["title"] == payload["title"]
    assert validate_board["description"] == payload["description"]

def test_get_board_not_found(client):

    non_existent_board_id = 999999

    response = client.get(f"/boards/{non_existent_board_id}")
    assert response.status_code == 404
    assert "not found" in response.json().get("detail", "").lower()

def test_update_board(client):
    payload = {
        "title": "Updating a test board",
        "description": "Updating a test board"
    }

    create_response = client.post("/boards/", json=payload)
    assert create_response.status_code == 201

    board_id = create_response.json()["board_id"]

    update_payload = {
        "title": "Updated a test board",
        "description": "This board has been updated"
    }

    update_response = client.put(f"/boards/{board_id}", json=update_payload)
    assert update_response.status_code == 200

    updated_board = update_response.json()
    assert updated_board["board_id"] == board_id
    assert updated_board["title"] == update_payload["title"]
    assert updated_board["description"] == update_payload["description"]

def test_delete_board(client):
    payload = {
        "title": "Delete Board by board_id",
        "description": "Deleting my first board by it's board_id"
    }

    created_response = client.post("/boards/", json=payload)
    assert created_response.status_code == 201

    board_id = created_response.json()["board_id"]

    delete_response = client.delete(f"/boards/{board_id}")
    assert delete_response.status_code in (200, 204)

    get_response = client.get(f"/boards/{board_id}")
    assert get_response.status_code == 404



