from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from MiniTrello.backend.app.database import Base
from datetime import datetime

class User(Base):
        __tablename__ = "Users"

        user_id = Column(Integer, primary_key=True, index=True)
        email = Column(String(255), unique=True, nullable=False)
        password_hash = Column(String(255), nullable=False)
        first_name = Column(String(100), nullable=False)
        last_name = Column(String(100), nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)
        is_active = Column(Boolean, default=True)

        comments = relationship("Comment", back_populates="user")

class Board(Base):
    __tablename__ = "Boards"

    board_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("Users.user_id"), index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    columns = relationship("BoardColumn", back_populates="board", lazy="joined")

class BoardColumn(Base):
    __tablename__ = "Columns"

    column_id = Column(Integer, primary_key=True, index=True)
    board_id = Column(Integer, ForeignKey("Boards.board_id"), index=True)
    title = Column(String(100), nullable=False)
    position = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    board = relationship("Board", back_populates="columns")
    tasks = relationship("Task", back_populates="column", lazy="joined")

class Task(Base):
    __tablename__ = "Tasks"

    task_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("Users.user_id"), index=True)
    column_id = Column(Integer, ForeignKey("Columns.column_id"), index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500))
    position = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    due_date = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)
    priority = Column(String(10))

    column = relationship("BoardColumn", back_populates="tasks")
    comments = relationship("Comment", back_populates="task", lazy="joined")

class Comment(Base):
    __tablename__ = "Comments"

    comment_id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("Tasks.task_id"), index=True)
    user_id = Column(Integer, ForeignKey("Users.user_id"), index=True)
    content = Column(String(500), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    task = relationship("Task", back_populates="comments")
    user = relationship("User",back_populates="comments", lazy="joined")


