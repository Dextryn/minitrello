import pytest

def test_create_board_column(client):
    board_payload = {
        "title": "Board for column test",
        "description": "Board used for column creation"
    }

    board_response = client.post("/boards/", json=board_payload)
    assert board_response.status_code == 201
    board_id = board_response.json()["board_id"]

    column_payload = {
        "title": "Create Board Column",
        "position": 1,
        "board_id": board_id
    }

    column_response = client.post("/columns/", json=column_payload)
    assert column_response.status_code == 201

    data = column_response.json()

    assert data["title"] == column_payload["title"]
    assert data["position"] == column_payload["position"]
    assert data["board_id"] == column_payload["board_id"]
    assert "column_id" in data
    assert "created_at" in data
    assert "updated_at" in data

def test_get_board_column_by_id(client):
    board_payload = {
        "title": "Creating Board for get_board_column_by_id",
        "description": "This board is being created to showcase the test_get_board_column_by_id"
    }

    board_response = client.post("/boards/", json=board_payload)
    assert board_response.status_code == 201
    board_id = board_response.json()["board_id"]

    column_payload = {
        "title": "This is my test_get_board_column_by_id",
        "position": 1,
        "board_id": board_id
    }

    column_response = client.post("/columns/", json=column_payload)
    assert column_response.status_code == 201

    created_column = column_response.json()
    column_id = created_column["column_id"]

    get_column = client.get(f"/columns/{column_id}")

    validate_column = get_column.json()

    assert validate_column["column_id"] == column_id
    assert validate_column["title"] == column_payload["title"]
    assert validate_column["position"] == column_payload["position"]

def test_get_board_column_by_board_id(client):
    board_payload = {
        "title": "Creating Board for get_board_column_by_board_id",
        "description": "This board is being created to showcase the test_get_board_column_by_id"
    }

    board_response = client.post("/boards/", json=board_payload)
    assert board_response.status_code == 201
    board_id = board_response.json()["board_id"]

    column_payload = {
        "title": "This is my test_get_board_column_by_board_id",
        "position": 1,
        "board_id": board_id
    }

    column_response = client.post("/columns/", json=column_payload)
    assert column_response.status_code == 201

    get_column = client.get(f"/columns/boards/{board_id}")
    assert get_column.status_code == 200

    validate_columns = get_column.json()

    validate_column = next(b for b in validate_columns if b["title"] == column_payload["title"])

    assert validate_column["board_id"] == board_id
    assert validate_column["title"] == column_payload["title"]
    assert validate_column["position"] == column_payload["position"]

def test_get_board_column_not_found(client):

    non_existent_column_id = 999999

    response = client.get(f"/columns/{non_existent_column_id}")
    assert response.status_code == 404
    assert "not found" in response.json().get("detail", "").lower()

def test_update_board_column(client):

    board_payload = {
        "title": "Creating Board for test_update_board_column",
        "description": "This board is being created to showcase the test_update_board_column"
    }

    board_response = client.post("/boards/", json=board_payload)
    assert board_response.status_code == 201
    board_id = board_response.json()["board_id"]

    column_payload = {
        "title": "Creating Column for test_update_board_column",
        "position": 1,
        "board_id": board_id
    }

    column_response = client.post("/columns", json=column_payload)
    assert column_response.status_code == 201
    column_id = column_response.json()["column_id"]

    update_payload = {
        "title": "Updating this Column for test_update_board_column"
    }

    update_response = client.put(f"/columns/{column_id}", json=update_payload)
    assert update_response.status_code == 200

    updated_board_column = update_response.json()
    assert updated_board_column["column_id"] == column_id
    assert updated_board_column["title"] == update_payload["title"]

def test_delete_board_column(client):
    board_payload = {
        "title": "Creating Board for test_delete_board_column",
        "description": "This board is being created to showcase the test_delete_board_column"
    }

    board_response = client.post("/boards/", json=board_payload)
    assert board_response.status_code == 201
    board_id = board_response.json()["board_id"]

    column_payload = {
        "title": "Creating this Column for test_delete_board_column",
        "position": 1,
        "board_id": board_id
    }

    column_response = client.post("/columns/", json=column_payload)
    assert column_response.status_code == 201
    column_id = column_response.json()["column_id"]

    delete_response = client.delete(f"/columns/{column_id}")
    assert delete_response.status_code in (200, 204)

    get_response = client.get(f"/columns/{column_id}")
    assert get_response.status_code == 404