from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from MiniTrello.backend.app.database import get_db
from MiniTrello.backend.app.schemas import CommentCreate, CommentUpdate, CommentOut
from MiniTrello.backend.app.crud import create_comment, get_comments, get_comment_by_id, get_comment_by_user_id, get_comment_by_task_id, update_comment, delete_comment

router = APIRouter(
    prefix="/comments",
    tags=["comments"]
)

### CREATE COMMENT
@router.post("/", response_model=CommentOut, status_code=201)
def create_new_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    return create_comment(
        db,
        task_id=comment.task_id,
        user_id=comment.user_id,
        content=comment.content
    )

### READ ALL COMMENTS
@router.get("/", response_model=List[CommentOut])
def read_comments(db: Session = Depends(get_db)):
    return get_comments(db)

### READ COMMENT BY ID
@router.get("/{comment_id}", response_model=CommentOut)
def read_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = get_comment_by_id(db, comment_id)
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

### READ COMMENT BY USER ID
@router.get("/users/{user_id}", response_model=List[CommentOut])
def read_comment_by_user_id(user_id: int, db: Session = Depends(get_db)):
    db_comment = get_comment_by_user_id(db, user_id)
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

### READ COMMENT BY TASK ID
@router.get("/tasks/{task_id}", response_model=List[CommentOut])
def read_comment_by_task_id(task_id: int, db: Session = Depends(get_db)):
    db_comment = get_comment_by_task_id(db, task_id)
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

### UPDATE COMMENT
@router.put("/{comment_id}", response_model=CommentOut)
def update_existing_comment(comment_id: int, comment: CommentUpdate, db: Session = Depends(get_db)):
    db_comment = update_comment(
        db,
        comment_id=comment_id,
        content=comment.content,
        is_active=comment.is_active
    )
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

### DELETE COMMENT
@router.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_comment(comment_id: int, db: Session = Depends(get_db)):
    result = delete_comment(db, comment_id)
    if not result:
        raise HTTPException(status_code=404, detail="Comment not found")
    return None