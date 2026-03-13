from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from MiniTrello.backend.app.routers import users, boards, columns, tasks, comments

app = FastAPI(title="MiniTrello API")

# --- CORS setup ---
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allow frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # allow all headers
)

@app.get("/")
def read_root():
    return {"message": "Mini Trello API is running!"}

app.include_router(users.router)
app.include_router(boards.router)
app.include_router(columns.router)
app.include_router(tasks.router)
app.include_router(comments.router)
