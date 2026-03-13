import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Boards from "./components/Boards/Boards.jsx";
import BoardsPage from "./components/BoardsPage/BoardsPage.jsx";
import TasksPage from "./components/TasksPage/TasksPage.jsx";
import CommentsPage from "./components/CommentsPage/CommentsPage.jsx";

function App() {
  return (
    <Router>
      <div className="App">
        <h1 className="app-title">
          Mini Trello - Project Management Application
        </h1>

        <Routes>
          <Route path="/" element={<Boards />} />
          <Route path="/boards/:board_id" element={<BoardsPage />} />
          <Route path="/boards/:board_id/columns/:column_id/tasks" element={<TasksPage />} />
          <Route path="/tasks/:task_id" element={<CommentsPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;