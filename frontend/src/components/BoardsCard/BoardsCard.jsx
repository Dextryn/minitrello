import React from "react";
import { Link } from  "react-router-dom";
import Columns from "../Columns/Columns";
import "./BoardsCard.css"; // optional: card-specific styles

const BoardsCard = ({ board, onDeleteClick}) => {

    return (
        <Link to={`/boards/${board.board_id}`} className="board-link">
        <div className="board-card">
            <div className="board-title">{board.title}</div>
            <div className="board-actions">
                <button className="btn btn-danger" onClick={onDeleteClick}>
                    Delete Board
                </button>
            </div>  
        </div>
        </Link>
    );
};

export default BoardsCard;
