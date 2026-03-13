import React, { useState, useEffect } from "react";
import "./Boards.css";
import BoardsCard from "../BoardsCard/BoardsCard.jsx";

const Boards = () => {
  const [boards, setBoards] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const [showModal, setShowModal] = useState(false);
  const [newBoardTitle, setNewBoardTitle] = useState("");
  const [newBoardDescription, setNewBoardDescription] = useState("");

  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [boardToDelete, setBoardToDelete] = useState(null);

  const [adding, setAdding] = useState(false);
  const [deleting, setDeleting] = useState(false);


  useEffect(() => {
    const fetchBoards = async () => {
      try {
        const res = await fetch("http://127.0.0.1:8000/boards/");
        if (!res.ok) throw new Error("Failed to fetch boards");
        const data = await res.json();
        setBoards(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchBoards();
  }, []);

// Add Board

  const addBoard = async () => {
    if (!newBoardTitle.trim()) return;

    try {
      setAdding(true);
      setError(null);

      const res = await fetch("http://127.0.0.1:8000/boards/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          title: newBoardTitle,
          description: newBoardDescription,
        }),
      });

      if (!res.ok) throw new Error("Failed to create board");

      const newBoard = await res.json();
      setBoards((prev) => [...prev, newBoard]);
      setNewBoardTitle("");
      setNewBoardDescription("");
      setShowModal(false);
    } catch (err) {
      setError(err.message);
    } finally {
      setAdding(false);
    }
  };

// Delete Board

  const deleteBoard = async (board_id) => {
    try {
      setError(null);

      const res = await fetch(`http://127.0.0.1:8000/boards/${board_id}`, {
        method: "DELETE",
      });

      if (!res.ok) throw new Error("Failed to delete board");

      setBoards((prev) => prev.filter(board => board.board_id !== board_id)
      );

    } catch (err) {
      setError(err.message);
    }

  };

  if (loading) return <div>Loading boards...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <div className="boards-top-row">
      <div className="boards-header">
      <h2>IS Business Systems - Projects</h2>
      </div>

      <div className="board-create-button">
        <button className="btn btn-primary" onClick={() => setShowModal(true)}>
         Create Board
        </button>
      </div>
      </div>
      <div className="boards-wrapper">
      <div className="board-container">
        {boards.map((board) => (
          <BoardsCard key={board.board_id} board={board} onDeleteClick={() => {
            setBoardToDelete(board);
            setShowDeleteModal(true);
          }} />
        ))}
      </div>
      </div>
        {showModal && (
          <div className="modal-overlay">
            <div className="modal-content">
              <h3>Create New Board</h3>
              <label>
                Title:
                <input
                type="text"
                value={newBoardTitle}
                onChange={(e) => setNewBoardTitle(e.target.value)}
                placeholder="Enter board title here."
                />
              </label>
              <br></br>
              <label>
                Description:
                <textarea
                className="board-description-textarea"
                value={newBoardDescription}
                onChange={(e) => setNewBoardDescription(e.target.value)}
                placeholder="Enter board description here."
                />
              </label>
              <div className="modal-actions">
                <button className="btn btn-danger"
                onClick={() => setShowModal(false)}
                >
                  Cancel
                </button>
                <button
                  className="btn btn-primary"
                  onClick={addBoard}
                  disabled={!newBoardTitle.trim()}
                  >
                  Create Board
                </button>
              </div>
            </div>
          </div>
          )}
          {showDeleteModal && boardToDelete && (
            <div className="modal-overlay">
              <div className="modal-content">
                <h3>Confirm Delete</h3>
                <p>Are you sure you want to delete "{boardToDelete.title}" Board?</p>
                <div className="modal-actions">
                  <button
                    className="btn btn-secondary"
                    onClick={() => setShowDeleteModal(false)}
                  >
                    Cancel
                  </button>
                  <button
                    className="btn btn-danger"
                    onClick={async () => {
                      await deleteBoard(boardToDelete.board_id);
                      setShowDeleteModal(false);
                      setBoardToDelete(null);
                    }}
                  >
                    Yes, Delete
                  </button>
                </div>
              </div>
            </div>
        )}
      </div>
  );
};

export default Boards;