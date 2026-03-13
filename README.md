# MiniTrello - Fullstack Project Management Application

MiniTrello is a fullstack web application inspired by Trello for managing projects, tasks, columns, and comments. This project is built with **FastAPI** for the backend and **React** for the frontend.

**STILL IN DEVELOPMENT**

---

## 🛠 Tech Stack

- **Backend:** FastAPI, Python, SQLAlchemy, SQLite/SQL Server
- **Frontend:** React, JavaScript, Vite, CSS
- **Database:** SQL Server / SQLite (development)
- **Version Control:** Git & GitHub

---

## 📁 Project Structure
MiniTrello/
├─ backend/        # FastAPI backend code
├─ frontend/       # React frontend code
├─ .gitignore
└─ README.md


---

## 🚀 Features

- Create, read, update, delete **boards**
- Create, read, update, delete **columns** inside boards
- Create, read, update, delete **tasks** inside columns
- Add **comments** to tasks
- Track task priority, due dates, and positions

---

## ⚙️ Setup & Installation

```bash
1. Clone the repo:
git clone git@github.com:Dextryn/minitrello.git
cd MiniTrello

2. Backend Setup:
cd backend
python -m venv venv
# Activate venv:
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

3. Frontend Setup
cd frontend
npm install
npm run dev


Notes:
1. Database configuration can be updated in backend/app/database.py
2. Ensure .env or other secrets are handled safely for production

Author:
Max Sommerville - https://github.com/Dextryn