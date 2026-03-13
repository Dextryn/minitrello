import React, {useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "./Tasks.css";

const Tasks = ({ tasks = [], board_id, column_id}) => {

    console.log("Tasks Info:", tasks);

    if (!tasks.length) return <div>No tasks found.</div>

    return (
        <div className="tasks-container">
            {tasks.map((task) => (
                <div key={task.task_id} className="task">
                        <div className="task-header">
                            <Link
                            to={`/tasks/${task.task_id}`}
                            className="task-link"
                            >
                                <h5>{task.title || "Untitled Task"}</h5>
                            </Link>
                        </div>
                </div>
            ))}
        </div>
    );
};

export default Tasks;