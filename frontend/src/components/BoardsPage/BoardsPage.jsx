import { useParams } from "react-router-dom";
import {useEffect, useState} from "react";
import Columns from "../Columns/Columns.jsx";

const BoardsPage = () =>{
    const { board_id } = useParams();
    const [board, setBoard] = useState(null);

    useEffect(() => {
        const fetchBoard = async () => {
            try {
            const res = await fetch(`http://127.0.0.1:8000/boards/${board_id}`);
            if (!res.ok) throw new Error("Failed to fetch board");
            const data = await res.json();
            setBoard(data);
        } catch (err) {
            console.error(err);
        }
        };

        fetchBoard();
    }, [board_id]);

    if (!board) return <div>Loading...</div>

    return(
        <div className="boards-page">
            <h2>{board.title}</h2>
            <h3>{board.description}</h3>

            {board.columns && board.columns.length > 0 ? (
                <Columns columns={board.columns} 
                board_id={board_id}
                />
                ) : (
                    <div>No Columns yet. Add one!</div>
            )}
        </div>
    );
};

export default BoardsPage;