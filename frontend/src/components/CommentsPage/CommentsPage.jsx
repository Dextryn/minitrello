import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import Comments from "../Comments/Comments.jsx";

const CommentsPage = () => {
    const { task_id } = useParams();
    const [task, setTask] = useState(null);

    useEffect(() => {
        const fetchTask = async () => {
            try {
                const res = await fetch(`http://127.0.0.1:8000/tasks/${task_id}`);
                if (!res.ok) throw new Error("Failed to fetch task");
                const data = await res.json();
                setTask(data);
            } catch (err) {
                console.error(err);
            }
        };
        

        fetchTask();
    }, [task_id]);

    if (!task) return <div>Loading...</div>;

    return (
        <div className="comments-page">
            <h2>{task.title}</h2>
            <p>{task.description}</p>

            <Comments
                comments={task.comments}
                task_id={task.task_id}
            />
        </div>
    );
};

export default CommentsPage;