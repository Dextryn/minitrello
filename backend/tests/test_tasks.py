import pytest
from datetime import datetime

def test_create_task(client):

    board_payload = {
        "title": "Creating this Board for test_create_task",
        "description": "This Board was created for test_create_task",
    }

    board_response = client.post("/boards/", json=board_payload)
    assert board_response.status_code == 201
    board_id = board_response.json()["board_id"]

    column_payload = {
        "title": "Creating this Column for test_create_task",
        "position": 1,
        "board_id": board_id
    }

    column_response = client.post("/columns/", json=column_payload)
    assert column_response.status_code == 201
    column_id = column_response.json()["column_id"]

    task_payload = {
        "title": "Creating this task for test_create_task",
        "description": "This task was created for test_create_task",
        "position": 1,
        "due_date": "2026-01-12T00:00:00",
        "priority": "Medium",
        "user_id": 21,
        "column_id": column_id
    }

    task_response = client.post("/tasks/", json=task_payload)
    assert task_response.status_code == 201

    data = task_response.json()

    assert data["title"] == task_payload["title"]
    assert data["description"] == task_payload["description"]
    assert data["position"] == task_payload["position"]
    assert data["due_date"] == task_payload["due_date"]
    assert data["priority"] == task_payload["priority"]
    assert data["user_id"] == task_payload["user_id"]
    assert data["column_id"] == column_id


def test_get_task_by_id(client):

    board_payload = {
        "title": "Creating this Board for test_get_task_by_id",
        "description": "This Board was created for test_get_task_by_id",
    }

    board_response = client.post("/boards/", json=board_payload)
    assert board_response.status_code == 201
    board_id = board_response.json()["board_id"]

    column_payload = {
        "title": "Creating this Column for test_get_task_by_id",
        "position": 1,
        "board_id": board_id
    }

    column_response = client.post("/columns/", json=column_payload)
    assert column_response.status_code == 201
    column_id = column_response.json()["column_id"]

    task_payload = {
        "title": "Creating this task for test_get_task_by_id",
        "description": "This task was created for test_get_task_by_id",
        "position": 1,
        "due_date":"2026-01-12T12:00:00",
        "priority": "Medium",
        "user_id": 21,
        "column_id": column_id
    }

    task_response = client.post("/tasks/", json=task_payload)
    assert task_response.status_code == 201
    task_id = task_response.json()["task_id"]

    get_task = client.get(f"/tasks/{task_id}")
    assert get_task.status_code == 200

    validate_task = get_task.json()

    assert validate_task["title"] == task_payload["title"]
    assert validate_task["description"] == task_payload["description"]
    assert validate_task["position"] == task_payload["position"]
    assert validate_task["due_date"] == task_payload["due_date"]
    assert validate_task["priority"] == task_payload["priority"]
    assert validate_task["user_id"] == task_payload["user_id"]
    assert validate_task["column_id"] == column_id

def test_get_task_by_user_id(client):

    board_payload = {
        "title": "Creating this Board for test_get_task_by_user_id",
        "description": "This Board was created for test_get_task_by_user_id",
    }

    board_response = client.post("/boards/", json=board_payload)
    assert board_response.status_code == 201
    board_id = board_response.json()["board_id"]

    column_payload = {
        "title": "Creating this Column for test_get_task_by_user_id",
        "position": 1,
        "board_id": board_id
    }

    column_response = client.post("/columns/", json=column_payload)
    assert column_response.status_code == 201
    column_id = column_response.json()["column_id"]

    task_payload = {
        "title": "Creating this task for test_get_task_by_user_id",
        "description": "This task was created for test_get_task_by_user_id",
        "position": 1,
        "due_date":"2026-01-12T12:00:00",
        "priority": "Medium",
        "user_id": 21,
        "column_id": column_id
    }

    task_response = client.post("/tasks/", json=task_payload)
    assert task_response.status_code == 201
    task_id = task_response.json()["task_id"]
    user_id = task_response.json()["user_id"]

    get_task = client.get(f"/tasks/users/{user_id}")
    assert get_task.status_code == 200

    validate_tasks = get_task.json()

    matching_tasks = [t for t in validate_tasks if t["task_id"] == task_id]
    assert len(matching_tasks) == 1

    validate_task = matching_tasks[0]

    assert validate_task["title"] == task_payload["title"]
    assert validate_task["description"] == task_payload["description"]
    assert validate_task["position"] == task_payload["position"]
    assert validate_task["due_date"] == task_payload["due_date"]
    assert validate_task["priority"] == task_payload["priority"]
    assert validate_task["user_id"] == task_payload["user_id"]
    assert validate_task["column_id"] == column_id

def test_get_task_by_column_id(client):

    board_payload = {
        "title": "Creating this Board for test_get_task_by_column_id",
        "description": "This Board was created for test_get_task_by_column_id",
    }

    board_response = client.post("/boards/", json=board_payload)
    assert board_response.status_code == 201
    board_id = board_response.json()["board_id"]

    column_payload = {
        "title": "Creating this Column for test_get_task_by_column_id",
        "position": 1,
        "board_id": board_id
    }

    column_response = client.post("/columns/", json=column_payload)
    assert column_response.status_code == 201
    column_id = column_response.json()["column_id"]

    task_payload = {
        "title": "Creating this task for test_get_task_by_column_id",
        "description": "This task was created for test_get_task_by_column_id",
        "position": 1,
        "due_date":"2026-01-12T12:00:00",
        "priority": "High",
        "user_id": 21,
        "column_id": column_id
    }

    task_response = client.post("/tasks/", json=task_payload)
    assert task_response.status_code == 201
    task_id = task_response.json()["task_id"]

    get_task = client.get(f"/tasks/columns/{column_id}")
    assert get_task.status_code == 200

    validate_tasks = get_task.json()

    matching_tasks = [t for t in validate_tasks if t["task_id"] == task_id]
    assert len(matching_tasks) == 1

    validate_task = matching_tasks[0]

    assert validate_task["title"] == task_payload["title"]
    assert validate_task["description"] == task_payload["description"]
    assert validate_task["position"] == task_payload["position"]
    assert validate_task["due_date"] == task_payload["due_date"]
    assert validate_task["priority"] == task_payload["priority"]
    assert validate_task["user_id"] == task_payload["user_id"]
    assert validate_task["column_id"] == column_id

def test_get_task_not_found(client):
    non_existent_task_id  = 999999

    response = client.get(f"/tasks/{non_existent_task_id}")
    assert response.status_code == 404
    assert "not found" in response.json().get("detail", "").lower()

def test_update_task(client):

    board_payload = {
        "title": "Creating this board for test_update_task",
        "description": "This Board was created for test_update_task"
    }

    board_response = client.post("/boards/", json=board_payload)
    assert board_response.status_code == 201
    board_id = board_response.json()["board_id"]

    column_payload = {
        "title": "Creating this Column for test_update_task",
        "position": 1,
        "board_id": board_id
    }

    column_response = client.post("/columns/", json=column_payload)
    assert column_response.status_code == 201
    column_id = column_response.json()["column_id"]

    task_payload = {
        "title": "Creating this Task for test_update_task",
        "description": "This Task was created for test_update_task",
        "position": 1,
        "due_date": "2026-01-12T12:00:00",
        "priority": "High",
        "user_id": 21,
        "column_id": column_id
    }

    task_response = client.post("/tasks/", json=task_payload)
    assert task_response.status_code == 201
    task_id = task_response.json()["task_id"]

    update_payload = {
        "title": "Updated this Task for test_update_task",
        "description": "This Task was updated for test_update_task",
        "priority": "Low"
    }

    update_response = client.put(f"/tasks/{task_id}", json=update_payload)
    assert update_response.status_code == 200

    updated_task = update_response.json()
    assert updated_task["task_id"] == task_id
    assert updated_task["title"] == update_payload["title"]
    assert updated_task["priority"] == update_payload["priority"]
    assert updated_task["description"] == update_payload["description"]
    ## unchanged fields
    assert updated_task["position"] == task_payload["position"]
    assert updated_task["user_id"] == task_payload["user_id"]
    assert updated_task["column_id"] == column_id
    assert updated_task["due_date"] == task_payload["due_date"]

def test_delete_task(client):

    board_payload = {
        "title": "Creating this Board for test_delete_task",
        "description": "This Board was created for test_delete_task"
    }

    board_response = client.post("/boards/", json=board_payload)
    assert board_response.status_code == 201
    board_id = board_response.json()["board_id"]

    column_payload = {
        "title": "Creating this Column for test_delete_task",
        "position": 1,
        "board_id": board_id
    }

    column_response = client.post("/columns/", json=column_payload)
    assert column_response.status_code == 201
    column_id = column_response.json()["column_id"]

    task_payload = {
        "title": "Creating this Task for test_delete_task",
        "description": "This Task was created for test_delete_task",
        "position": 1,
        "due_date": "2026-01-12T12:00:00",
        "priority": "Low",
        "user_id": 21,
        "column_id": column_id
    }

    task_response = client.post("/tasks/", json=task_payload)
    assert task_response.status_code == 201
    task_id = task_response.json()["task_id"]

    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code in (200, 204)

    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404