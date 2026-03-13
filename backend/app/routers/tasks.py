from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from MiniTrello.backend.app.database import get_db
from MiniTrello.backend.app.schemas import TaskCreate, TaskUpdate, TaskOut
from MiniTrello.backend.app.crud import create_task, get_tasks, get_task_by_id,get_task_by_user_id, get_task_by_column_id, update_task, delete_task

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

### CREATE TASK
@router.post("/", response_model=TaskOut, status_code=201)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(
        db,
        user_id=task.user_id,
        column_id=task.column_id,
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        position=task.position,
        priority=task.priority
    )

### READ ALL TASKS
@router.get("/", response_model=List[TaskOut])
def read_tasks(db: Session = Depends(get_db)):
    return get_tasks(db)

### READ TASK BY ID
@router.get("/{task_id}", response_model=TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = get_task_by_id(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

### READ TASK BY USER ID
@router.get("/users/{user_id}", response_model=List[TaskOut])
def read_task_by_user_id(user_id: int, db: Session = Depends(get_db)):
    db_task = get_task_by_user_id(db, user_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

### READ TASK BY COLUMN ID
@router.get("/columns/{column_id}", response_model=List[TaskOut])
def read_task_by_column_id(column_id: int, db: Session = Depends(get_db)):
    db_task = get_task_by_column_id(db, column_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

### UPDATE TASK
@router.put("/{task_id}", response_model=TaskOut)
def update_existing_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    db_task = update_task(
        db,
        task_id=task_id,
        user_id=task.user_id,
        column_id=task.column_id,
        title=task.title,
        description=task.description,
        position=task.position,
        due_date=task.due_date,
        is_active=task.is_active,
        priority=task.priority
    )
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

### DELETE TASK
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
    result = delete_task(db, task_id)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    return None