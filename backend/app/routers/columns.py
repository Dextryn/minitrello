from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from MiniTrello.backend.app.database import get_db
from MiniTrello.backend.app.schemas import BoardColumnCreate, BoardColumnUpdate, BoardColumnOut
from MiniTrello.backend.app.crud import create_column, get_board_columns, get_board_column_by_id, get_board_column_by_board_id, update_board_column, delete_board_column

router = APIRouter(
    prefix="/columns",
    tags=["columns"]
)

### CREATE BOARD COLUMN
@router.post("/", response_model=BoardColumnOut, status_code=201)
def create_new_board_column(board_column: BoardColumnCreate, db: Session = Depends(get_db)):
    return create_column(
        db,
        board_id=board_column.board_id,
        title=board_column.title,
        position=board_column.position
    )

### READ ALL BOARD COLUMNS
@router.get("/", response_model=List[BoardColumnOut])
def read_board_columns(db: Session = Depends(get_db)):
    return get_board_columns(db)

### READ BOARD COLUMN BY ID
@router.get("/{column_id}", response_model=BoardColumnOut)
def read_board_column(column_id: int, db: Session = Depends(get_db)):
    db_board_column = get_board_column_by_id(db, column_id)
    if not db_board_column:
        raise HTTPException(status_code=404, detail="Column not found")
    return db_board_column

### READ BOARD COLUMN BY BOARD ID
@router.get("/boards/{board_id}", response_model=List[BoardColumnOut])
def read_board_column_board_id(board_id: int, db: Session = Depends(get_db)):
    db_board_column = get_board_column_by_board_id(db, board_id)
    if not db_board_column:
        raise HTTPException(status_code=404, detail="Column not found")
    return db_board_column

### UPDATE BOARD COLUMN
@router.put("/{column_id}", response_model=BoardColumnOut)
def update_existing_board_column(column_id: int, board_column: BoardColumnUpdate, db: Session  = Depends(get_db)):
    db_board_column = update_board_column(
        db,
        column_id=column_id,
        title=board_column.title,
        position=board_column.position,
        is_active=board_column.is_active
    )
    if not db_board_column:
        raise HTTPException(status_code=404, detail="Column not found")
    return db_board_column

### DELETE BOARD COLUMN
@router.delete("/{column_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_board_column(column_id: int, db: Session = Depends(get_db)):
    result = delete_board_column(db, column_id)
    if not result:
        raise HTTPException(status_code=404, detail="Column not found")
    return None
