import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import Tasks from "../Tasks/Tasks.jsx";

const TasksPage = () => {
    const { column_id, title } = useParams();
    const [column, setColumn] = useState(null);

    useEffect(() => {
        const fetchColumn = async () => {
            try {
                const res = await fetch(`http://127.0.0.1:8000/columns/${column_id}/`);
                if (!res.ok) throw new Error("Failed to fetch column");
                const data = await res.json();
                setColumn(data);
            } catch (err) {
                console.error(err);
            }
        };

        fetchColumn();
    }, [column_id]);

    if (!column) return <div>Loading...</div>;

    return (
        <div className="tasks-page">
            <h2>Tasks for Column {column.title}</h2>

            <Tasks
                tasks={column.tasks}
                column_id={column.column_id}
                board_id={column.board_id}
            />
        </div>
    );
};

export default TasksPage;