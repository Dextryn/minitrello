from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from typing import List

from MiniTrello.backend.app.database import get_db
from MiniTrello.backend.app.schemas import BoardCreate, BoardUpdate, BoardOut
from MiniTrello.backend.app.crud import create_board, get_boards, get_board_by_id, get_board_by_user_id, update_board, delete_board
from MiniTrello.backend.app.dependencies import get_current_user
from MiniTrello.backend.app.models import User, Board

router = APIRouter(
    prefix="/boards",
    tags=["boards"]
)

### CREATE BOARD
@router.post("/", response_model=BoardOut, status_code=201)
def create_new_board(board: BoardCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_board(
        db,
##        user_id=current_user.user_id,
        user_id=1,
        title=board.title,
        description=board.description
    )

### READ ALL BOARDS
@router.get("/", response_model=List[BoardOut])
def read_boards(db: Session = Depends(get_db)):
    return get_boards(db)

@router.get("/", response_model=List[BoardOut])
def get_all_boards(db: Session = Depends(get_db)):
    boards = (
        db.query(Board)
        .options(
            joinedload(Board.columns)
            .joinedload("tasks")
            .joinedload("comments")
            .joinedload("user")
        )
        .all()
    )

### READ BOARD BY ID
@router.get("/{board_id}", response_model=BoardOut)
def read_board(board_id: int, db: Session = Depends(get_db)):
    db_board = get_board_by_id(db, board_id)
    if not db_board:
        raise HTTPException(status_code=404, detail="Board not found")
    return db_board

### READ BOARD BY USER ID
@router.get("/user/{user_id}", response_model=List[BoardOut])
def read_board_by_user_id(user_id: int, db: Session = Depends(get_db)):
    db_boards = get_board_by_user_id(db, user_id)
    if not db_boards:
        raise HTTPException(status_code=404, detail="Board not found")
    return db_boards

### UPDATE BOARD
@router.put("/{board_id}", response_model=BoardOut)
def update_existing_board(board_id:int, board: BoardUpdate, db: Session = Depends(get_db)):
    db_board = get_board_by_id(db, board_id)
    if not db_board:
        raise HTTPException(status_code=404, detail="Board not found")

    updated_board = update_board (
        db,
        board_id=board_id,
        user_id=db_board.user_id,
        title=board.title,
        description=board.description,
        is_active=board.is_active
    )

    return updated_board

### DELETE BOARD
@router.delete("/{board_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete__existing_board(board_id: int, db: Session = Depends(get_db)):
    result = delete_board(db, board_id)
    if not result:
        raise HTTPException(status_code=404, detail="Board not found")
    return None