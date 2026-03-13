from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from MiniTrello.backend.app.database import get_db #session dependency
from MiniTrello.backend.app.schemas import UserCreate, UserUpdate, UserOut
from MiniTrello.backend.app.crud import create_user, get_users, get_user_by_id, update_user, delete_user

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

### CREATE USER
@router.post("/", response_model=UserOut, status_code=201)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(
        db,
        email=user.email,
        password_hash=user.password,
        first_name=user.first_name,
        last_name=user.last_name
    )

### READ ALL USERS
@router.get("/", response_model=List[UserOut])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

### READ USER BY ID
@router.get("/{user_id}", response_model=UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

### UPDATE USER
@router.put("/{user_id}", response_model=UserOut)
def update_existing_user(user_id:int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = update_user(
        db,
        user_id=user_id,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        is_active=user.is_active
    )
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

### DELETE USER
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_user(user_id:int, db: Session = Depends(get_db)):
    result = delete_user(db, user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return None