import pytest
from sqlalchemy.testing.suite.test_reflection import users


def test_create_comment(client):

    board_payload = {
        "title": "Creating this Board for test_create_comment",
        "description": "This Board was created for test_create_comment"
    }

    board_response = client.post("/boards/", json=board_payload)
    assert board_response.status_code == 201
    board_id = board_response.json()["board_id"]

    column_payload = {
        "title": "Creating this Column for test_create_comment",
        "position": 1,
        "board_id": board_id
    }

    column_response = client.post("/columns/", json=column_payload)
    assert column_response.status_code == 201
    column_id = column_response.json()["column_id"]

    task_payload = {
        "title": "Creating this Task for test_create_comment",
        "description": "This task was created for test_create_comment",
        "position": 1,
        "due_date": "2026-01-12T16:00:00",
        "priority": "High",
        "user_id": 21,
        "column_id": column_id
    }

    task_response = client.post("/tasks/", json=task_payload)
    assert task_response.status_code == 201
    task_id = task_response.json()["task_id"]
    user_id = task_response.json()["user_id"]

    comment_payload = {
        "task_id": task_id,
        "user_id": user_id,
        "content": "This Comment was created for test_create_comment"
    }

    comment_response = client.post("/comments/", json=comment_payload)
    assert comment_response.status_code == 201
    comment_id = comment_response.json()["comment_id"]

    data = comment_response.json()

    assert data["comment_id"] == comment_id
    assert data["task_id"] == task_id
    assert data["user_id"] == user_id
    assert data["content"] == comment_payload["content"]

def test_get_comment_by_id(client):

    board_payload = {
        "title": "Creating this Board for test_get_comment_by_id",
        "description": "This Board was created for test_get_comment_by_id",
    }

    board_response = client.post("/boards/", json=board_payload)
    assert board_response.status_code == 201
    board_id = board_response.json()["board_id"]

    column_payload = {
        "title": "Creating this Column for test_get_comment_by_id",
        "position": 1,
        "board_id": board_id
    }

    column_response = client.post("/columns/", json=column_payload)
    assert column_response.status_code == 201
    column_id = column_response.json()["column_id"]

    task_payload = {
        "title": "Creating this Task for test_get_comment_by_id",
        "description": "This task was created for test_get_comment_by_id",
        "position": 1,
        "due_date": "2026-01-16T12:00:00",
        "priority": "Medium",
        "user_id": 21,
        "column_id": column_id
    }

    task_response = client.post("/tasks/", json=task_payload)
    assert task_response.status_code == 201
    task_id = task_response.json()["task_id"]
    user_id = task_response.json()["user_id"]

    comment_payload = {
        "task_id": task_id,
        "user_id": user_id,
        "content": "This Comment was created for test_get_comment_by_id"
    }

    comment_response = client.post("/comments/", json=comment_payload)
    assert comment_response.status_code == 201
    comment_id = comment_response.json()["comment_id"]

    get_comment = client.get(f"/comments/{comment_id}")
    assert get_comment.status_code == 200

    validate_comment = get_comment.json()

    assert validate_comment["task_id"] == task_id
    assert validate_comment["user_id"] == user_id
    assert validate_comment["content"] == comment_payload["content"]

def test_get_comment_by_user_id(client):

    board_payload = {
        "title": "Creating this Board for test_get_comment_by_user_id",
        "description": "This Board was created for test_get_comment_by_user_id",
    }

    board_response = client.post("/boards/", json=board_payload)
    assert board_response.status_code == 201
    board_id = board_response.json()["board_id"]

    column_payload = {
        "title": "Creating this Column for test_get_comment_by_user_id",
        "position": 1,
        "board_id": board_id
    }

    column_response = client.post("/columns/", json=column_payload)
    assert column_response.status_code == 201
    column_id = column_response.json()["column_id"]

    task_payload = {
        "title": "Creating this Task for test_get_comment_by_user_id",
        "description": "This task was created for test_get_comment_by_user_id",
        "position": 1,
        "due_date": "2026-01-16T12:00:00",
        "priority": "Medium",
        "user_id": 21,
        "column_id": column_id
    }

    task_response = client.post("/tasks/", json=task_payload)
    assert task_response.status_code == 201
    task_id = task_response.json()["task_id"]
    user_id = task_response.json()["user_id"]

    comment_payload = {
        "task_id": task_id,
        "user_id": user_id,
        "content": "This Comment was created for test_get_comment_by_user_id"
    }

    comment_response = client.post("/comments/", json=comment_payload)
    assert comment_response.status_code == 201
    comment_id = comment_response.json()["comment_id"]

    get_comment = client.get(f"/comments/users/{user_id}")
    assert get_comment.status_code == 200

    validate_comments = get_comment.json()

    matching_comments = [t for t in validate_comments if t["comment_id"] == comment_id]
    assert len(matching_comments) == 1

    validate_comment = matching_comments[0]

    assert validate_comment["task_id"] == task_id
    assert validate_comment["user_id"] == user_id
    assert validate_comment["content"] == comment_payload["content"]

def test_get_comment_by_task_id(client):

    board_payload = {
        "title": "Creating this Board for test_get_comment_by_task_id",
        "description": "This Board was created for test_get_comment_by_task_id",
    }

    board_response = client.post("/boards/", json=board_payload)
    assert board_response.status_code == 201
    board_id = board_response.json()["board_id"]

    column_payload = {
        "title": "Creating this Column for test_get_comment_by_task_id",
        "position": 1,
        "board_id": board_id
    }

    column_response = client.post("/columns/", json=column_payload)
    assert column_response.status_code == 201
    column_id = column_response.json()["column_id"]

    task_payload = {
        "title": "Creating this Task for test_get_comment_by_task_id",
        "description": "This task was created for test_get_comment_by_task_id",
        "position": 1,
        "due_date": "2026-01-16T12:00:00",
        "priority": "Medium",
        "user_id": 21,
        "column_id": column_id
    }

    task_response = client.post("/tasks/", json=task_payload)
    assert task_response.status_code == 201
    task_id = task_response.json()["task_id"]
    user_id = task_response.json()["user_id"]

    comment_payload = {
        "task_id": task_id,
        "user_id": user_id,
        "content": "This Comment was created for test_get_comment_by_task_id"
    }

    comment_response = client.post("/comments/", json=comment_payload)
    assert comment_response.status_code == 201

    get_comment = client.get(f"/comments/tasks/{task_id}")
    assert get_comment.status_code == 200

    validate_comments = get_comment.json()

    matching_comments = [t for t in validate_comments if t["task_id"] == task_id]
    assert len(matching_comments) == 1

    validate_comment = matching_comments[0]

    assert validate_comment["task_id"] == task_id
    assert validate_comment["user_id"] == user_id
    assert validate_comment["content"] == comment_payload["content"]

def test_get_comment_not_found(client):

    non_existent_comment_id = 999999

    response = client.get(f"/comments/{non_existent_comment_id}")
    assert response.status_code == 404
    assert "not found" in response.json().get("detail", "").lower()

def test_update_comment(client):

    board_payload = {
        "title": "Creating this Board for test_update_comment",
        "description": "This Board was created for test_update_comment",
    }

    board_response = client.post("/boards/", json=board_payload)
    assert board_response.status_code == 201
    board_id = board_response.json()["board_id"]

    column_payload = {
        "title": "Creating this Column for test_update_comment",
        "position": 1,
        "board_id": board_id
    }

    column_response = client.post("/columns/", json=column_payload)
    assert column_response.status_code == 201
    column_id = column_response.json()["column_id"]

    task_payload = {
        "title": "Creating this Task for test_update_comment",
        "description": "This task was created for test_update_comment",
        "position": 1,
        "due_date": "2026-01-16T12:00:00",
        "priority": "Medium",
        "user_id": 21,
        "column_id": column_id
    }

    task_response = client.post("/tasks/", json=task_payload)
    assert task_response.status_code == 201
    task_id = task_response.json()["task_id"]
    user_id = task_response.json()["user_id"]

    comment_payload = {
        "task_id": task_id,
        "user_id": user_id,
        "content": "This Comment was created for test_update_comment"
    }

    comment_response = client.post("/comments/", json=comment_payload)
    assert comment_response.status_code == 201
    comment_id = comment_response.json()["comment_id"]

    update_payload = {
        "content": "This comment was updated by test_update_comment"
    }

    update_response = client.put(f"/comments/{comment_id}", json=update_payload)
    assert update_response.status_code == 200

    update_comment = update_response.json()

    assert update_comment["task_id"] == task_id
    assert update_comment["user_id"] == user_id
    assert update_comment["content"] == update_payload["content"]

def test_delete_comment(client):

    board_payload = {
        "title": "Creating this Board for test_delete_comment",
        "description": "This Board was created for test_delete_comment",
    }

    board_response = client.post("/boards/", json=board_payload)
    assert board_response.status_code == 201
    board_id = board_response.json()["board_id"]

    column_payload = {
        "title": "Creating this Column for test_delete_comment",
        "position": 1,
        "board_id": board_id
    }

    column_response = client.post("/columns/", json=column_payload)
    assert column_response.status_code == 201
    column_id = column_response.json()["column_id"]

    task_payload = {
        "title": "Creating this Task for test_delete_comment",
        "description": "This task was created for test_delete_comment",
        "position": 1,
        "due_date": "2026-01-16T12:00:00",
        "priority": "Medium",
        "user_id": 21,
        "column_id": column_id
    }

    task_response = client.post("/tasks/", json=task_payload)
    assert task_response.status_code == 201
    task_id = task_response.json()["task_id"]
    user_id = task_response.json()["user_id"]

    comment_payload = {
        "task_id": task_id,
        "user_id": user_id,
        "content": "This Comment was created for test_delete_comment"
    }

    comment_response = client.post("/comments/", json=comment_payload)
    assert comment_response.status_code == 201
    comment_id = comment_response.json()["comment_id"]

    delete_comment = client.delete(f"/comments/{comment_id}")
    assert delete_comment.status_code in (200, 204)

    get_comment = client.get(f"/comments/{comment_id}")
    assert get_comment.status_code == 404