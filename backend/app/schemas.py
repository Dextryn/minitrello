from __future__ import annotations
from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

####### SCHEMA #######

### USERS
class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    is_active: bool | None = None

class UserOut(UserBase):
    user_id: int
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

### BOARDS
class BoardBase(BaseModel):
    title: str
    description: str

class BoardCreate(BoardBase):
    pass

class BoardUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    is_active: bool | None = None

class BoardOut(BoardBase):
    board_id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    is_active: bool
    columns: list["BoardColumnOut"] = []

    model_config = ConfigDict(from_attributes=True)

### COLUMNS
class BoardColumnBase(BaseModel):
    title: str
    position: int

class BoardColumnCreate(BoardColumnBase):
    board_id: int

class BoardColumnUpdate(BaseModel):
    title: str | None = None
    position: int | None = None
    is_active: bool | None = None


class BoardColumnOut(BoardColumnBase):
    column_id: int
    board_id: int
    created_at: datetime
    updated_at: datetime
    is_active: bool
    tasks: list["TaskOut"] = []

    model_config = ConfigDict(from_attributes=True)

### TASKS
class TaskBase(BaseModel):
    title: str
    description: str | None = None
    position: int
    due_date: datetime | None = None
    priority: str

class TaskCreate(TaskBase):
    user_id: int
    column_id: int

class TaskUpdate(BaseModel):
    user_id: int | None = None
    column_id: int | None = None
    title: str | None = None
    description: str | None = None
    position: int | None = None
    due_date: datetime | None = None
    is_active: bool | None = None
    priority: str | None = None

class TaskOut(TaskBase):
    task_id: int
    user_id: int
    column_id: int
    created_at: datetime
    updated_at: datetime
    is_active: bool
    comments: list["CommentOut"] = []

    model_config = ConfigDict(from_attributes=True)

### COMMENTS
class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    task_id: int
    user_id: int

class CommentUpdate(BaseModel):
    content: str | None = None
    is_active: bool | None = None

class CommentOut(CommentBase):
    comment_id: int
    task_id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    is_active: bool
    
    user: UserBase

    model_config = ConfigDict(from_attributes=True)

