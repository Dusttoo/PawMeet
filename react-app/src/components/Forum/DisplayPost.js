import React from "react";
import { useSelector } from "react-redux";
import "./Forum.css";
import { Link } from "react-router-dom";

const DisplayPosts = ({ post }) => {
  const authors = useSelector((state) => state.users);
  const author = Object.keys(authors).find(
    (thisAuthor) => +post.user_id === +thisAuthor
  );
  const comments = useSelector((state) => state.comments);
  const theseComments = [];
  Object.keys(comments).map((commentId) => {
    const comment = Object.values(comments).find(
      (thisComment) => +thisComment.id === +commentId
    );
    if (comment.post_id === post.id) {
      theseComments.push(comment);
    }
  });

  const modifyTime = () => {
    const date = post.posted.replace("00:00:00 GMT", "");
    return date;
  };

  return (
    <>
      <tr className="post-row">
        <td>
          <div className="comment-info">
            <Link to={`/users/${author}`}>
              <img
                className="profile-icon"
                src={authors[author].profile_img}
                alt={authors[author].first_name}
              />
            </Link>
            <Link className="user-name" to={`/users/${author}`}>
              {authors[author].first_name}
            </Link>
          </div>
        </td>
        <td>
          <Link to={`/forum/posts/${post.id}`} className="post-title">
            {post.title}
          </Link>
        </td>
        <td>{modifyTime()}</td>
        <td className="comment-count">{theseComments.length}</td>
      </tr>
    </>
  );
};

export default DisplayPosts;
