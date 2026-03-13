import React from "react";
import "./Comments.css";

const Comments = ({ comments = [] }) => {

  console.log("Comment info:", comments);

  if (!comments.length) {
    return <p className="no-comments">No comments yet</p>;
  }

  return (
    <div className="comments-container">
      {comments.map((comment) => (
        <div key={comment.comment_id} className="comment">
          <p className="comment-author">
            {comment.user?.first_name} {comment.user?.last_name}
          </p>
          <p className="comment-content">
            {comment.content}
          </p>
        </div>
      ))}
    </div>
  );
};

export default Comments;