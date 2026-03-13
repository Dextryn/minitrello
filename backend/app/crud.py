from fastapi import HTTPException

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from MiniTrello.backend.app.models import User, Board, BoardColumn, Task, Comment
from datetime import datetime

########## C-R-U-D ##########
########## CREATE ##########
def create_user(db: Session, email: str, password_hash: str, first_name: str, last_name: str):
    user = User(
        email=email,
        password_hash=password_hash,
        first_name=first_name,
        last_name=last_name
    )
    db.add(user)
    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="User already exists")
    return user

def create_board(db: Session, user_id: int, title: str, description: str = ""):
    board = Board(
        user_id=user_id,
        title=title,
        description=description
    )
    db.add(board)
    db.commit()
    db.refresh(board)
    return board

def create_column(db: Session, board_id: int, title: str, position: int):
    column = BoardColumn(
        board_id=board_id,
        title=title,
        position=position
    )
    db.add(column)
    db.commit()
    db.refresh(column)
    return column

def create_task(db: Session, user_id: int, column_id: int, title: str, position: int, priority: str, due_date: datetime, description: str = ""):
    task = Task(
        user_id=user_id,
        column_id=column_id,
        title=title,
        description=description,
        due_date=due_date,
        position=position,
        priority=priority
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def create_comment(db: Session, task_id: int, user_id: int, content: str):
    comment = Comment(
        task_id=task_id,
        user_id=user_id,
        content=content
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

########## READ ##########

## USERS
def get_user_by_id(db: Session, user_id: int):
    return db.get(User, user_id)

def get_users(db: Session):
    return db.query(User).all()

## BOARDS
def get_board_by_id(db:Session, board_id: int):
    return db.get(Board, board_id)

def get_board_by_user_id(db: Session, user_id: int):
    return db.query(Board).filter(Board.user_id == user_id).all()

def get_boards(db: Session):
    return db.query(Board).all()

## BOARD COLUMNS
def get_board_column_by_id(db:Session, column_id: int):
    return db.get(BoardColumn, column_id)

def get_board_column_by_board_id(db:Session, board_id:int):
    return db.query(BoardColumn).filter(BoardColumn.board_id == board_id).all()

def get_board_columns(db: Session):
    return db.query(BoardColumn).all()

## TASKS
def get_task_by_id(db: Session, task_id: int):
    return db.get(Task, task_id)

def get_task_by_user_id(db: Session, user_id):
    return db.query(Task).filter(Task.user_id == user_id).all()

def get_task_by_column_id(db: Session, column_id):
    return db.query(Task).filter(Task.column_id == column_id).all()

def get_tasks(db: Session):
    return db.query(Task).all()

## COMMENTS
def get_comment_by_id(db: Session, comment_id: int):
    return db.get(Comment, comment_id)

def get_comment_by_user_id(db: Session, user_id: int):
    return db.query(Comment).filter(Comment.user_id == user_id).all()

def get_comment_by_task_id(db: Session, task_id: int):
    return db.query(Comment).filter(Comment.task_id == task_id).all()

def get_comments(db: Session):
    return db.query(Comment).all()

########## UPDATE ##########

### USER UPDATE
def update_user(db: Session, user_id: int, email: str | None = None, first_name: str | None = None, last_name: str | None = None, is_active: bool | None = None):

    user = db.get(User, user_id)

    if not user:
        return None
    if email is not None:
        user.email = email
    if first_name is not None:
        user.first_name = first_name
    if last_name is not None:
        user.last_name = last_name
    if is_active is not None:
        user.is_active = is_active

    db.commit()
    db.refresh(user)

    return user

### BOARD UPDATE
def update_board(db: Session, board_id: int, user_id: int, title: str | None = None, description: str | None = None, is_active: bool | None = None):

    board = db.get(Board, board_id)

    if not board:
        return None
    if title is not None:
        board.title = title
    if description is not None:
        board.description = description
    if is_active is not None:
        board.is_active = is_active

    db.commit()
    db.refresh(board)

    return board

### BOARD COLUMN UPDATE
def update_board_column(db: Session, column_id: int, title: str | None = None, position: int | None = None, is_active: bool | None = None):

    board_column = db.get(BoardColumn, column_id)

    if not board_column:
        return None
    if title is not None:
        board_column.title = title
    if position is not None:
        board_column.position = position
    if is_active is not None:
        board_column.is_active = is_active

    db.commit()
    db.refresh(board_column)

    return board_column

### TASK UPDATE

def update_task(db: Session, task_id: int, user_id: int | None = None, column_id: int | None = None, title: str | None = None, description: str | None = None, position: int | None = None, due_date: datetime | None = None, is_active: bool | None = None, priority: str | None = None):

    task = db.get(Task, task_id)

    if not task:
        return None
    if user_id is not None:
        task.user_id = user_id
    if column_id is not None:
        task.column_id = column_id
    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    if position is not None:
        task.position = position
    if due_date is not None:
        task.due_date = due_date
    if is_active is not None:
        task.is_active = is_active
    if priority is not None:
        task.priority = priority

    db.commit()
    db.refresh(task)

    return task

def update_comment(db: Session, comment_id: int, content: str | None = None, is_active: bool | None = None):

    comment = db.get(Comment, comment_id)

    if not comment:
        return None
    if content is not None:
        comment.content = content
    if is_active is not None:
        comment.is_active = is_active

    db.commit()
    db.refresh(comment)

    return comment

########## DELETE ##########

### USER DELETE
def delete_user(db: Session, user_id: int):

    user = db.get(User, user_id)

    if not user:
        return None

    db.delete(user)
    db.commit()

    return True

### BOARD DELETE
def delete_board(db: Session, board_id: int):

    board = db.get(Board, board_id)

    if not board:
        return None

    db.delete(board)
    db.commit()

    return True

### BOARD COLUMN DELETE
def delete_board_column(db: Session, column_id:int):

    board_column = db.get(BoardColumn, column_id)

    if not board_column:
        return None

    db.delete(board_column)
    db.commit()

    return True

### TASK DELETE
def delete_task(db: Session, task_id: int):

    task = db.get(Task, task_id)

    if not task:
        return None

    db.delete(task)
    db.commit()

    return True

### COMMENT DELETE
def delete_comment(db: Session,comment_id: int):

    comment = db.get(Comment, comment_id)

    if not comment:
        return None

    db.delete(comment)
    db.commit()

    return True