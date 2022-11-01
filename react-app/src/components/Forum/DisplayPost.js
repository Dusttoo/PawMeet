import React from "react";
import { useSelector } from "react-redux";
import "./Forum.css";
import { Link } from "react-router-dom";

const DisplayPosts = ({ post }) => {
  const authors = useSelector((state) => state.users);
  const author = Object.values(authors).find(
    (thisAuthor) => post.user_id === thisAuthor.id
  );
  const comments = useSelector((state) => state.comments);
  const eachPostComments = Object.values(comments).filter(
    (thisComment) => thisComment.post_id === post.id
  );

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
                src={author.profile_img}
                alt={author.first_name}
              />
            </Link>
            <Link className="user-name" to={`/users/${author.id}`}>
              {author.first_name}
            </Link>
          </div>
        </td>
        <td>
          <Link to={`/forum/posts/${post.id}`} className="post-title">
            {post.title}
          </Link>
        </td>
        <td>{modifyTime()}</td>
        <td className="comment-count">{eachPostComments.length}</td>
      </tr>
    </>
  );
};

export default DisplayPosts;
