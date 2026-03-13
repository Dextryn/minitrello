import React from "react";
import { Link } from "react-router-dom";
import "./Columns.css";

const Columns = ({ columns = [], board_id }) => {
  if (!columns.length) return <div>No columns found.</div>;

  return (
    <div className="columns-container">
      {columns.map((col) => (
        <div key={col.column_id} className="column">
          <div className="column-header">
            <div className="columns-header">
            <Link 
              to={`/boards/${board_id}/columns/${col.column_id}/tasks`} 
              className="column-link"
            >
              <h5>{col.title || "Untitled Column"}</h5>
            </Link>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default Columns;