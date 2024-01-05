import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { useSelector } from "react-redux";
import "./Forum.css";
import { Link } from "react-router-dom";
import { useParams } from "react-router";
import { removeComment } from "../../store/post_comments";
import EditComment from "./EditComment";
import { postComments } from "../../store/post_comments";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPen, faMinusCircle } from "@fortawesome/free-solid-svg-icons";

const DisplayComments = ({ commentId }) => {
  const { postId } = useParams();
  const dispatch = useDispatch();
  const authors = useSelector((state) => state.users);
  const theseComments = useSelector((state) => state.post_comments);
  const currentUser = useSelector((state) => state.session.user);
  const [editForm, setEditForm] = useState(false);
  const [loaded, setLoaded] = useState(false);
  const comment = Object.keys(theseComments).find(
    (comment) => +comment === commentId
  );
  let author = 0;

  useEffect(() => {
    (async () => {
      await dispatch(postComments(postId));

      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  if (comment) {
    author = Object.keys(authors).find(
      (thisAuthor) => +theseComments[comment].user_id === +thisAuthor
    );
  } else {
    return null;
  }

  const deleteComment = () => {
    dispatch(removeComment(theseComments[comment].id));
  };

  const openEditForm = () => {
    if (editForm) {
      setEditForm(false);
    } else {
      setEditForm(true);
    }
  };

  const modifyTime = () => {
    const date = theseComments[comment].posted.replace("00:00:00 GMT", "");
    return date;
  };

  return (
    <>
      {Object.keys(theseComments) ? <></> : <h2>No comments to display</h2>}
      <tr className="comment-row">
        <td className="comment-cell">
          <div className="comment-info">
            <Link to={`/users/${author}`}>
              <img
                className="profile-icon"
                src={authors[author].profile_img}
                alt={authors[author].name}
              />
            </Link>
            <div className="name-date">
              <Link className="author-name" to={`/users/${author}`}>
                {authors[author].first_name} {authors[author].last_name}
              </Link>
              {modifyTime()}
            </div>
          </div>
          {+authors[author].id === +currentUser.id ? (
            <td className="comment-edit-delete">
              <FontAwesomeIcon
                icon={faPen}
                className="edit-button"
                onClick={openEditForm}
              />
              <FontAwesomeIcon
                icon={faMinusCircle}
                className="delete-button"
                onClick={deleteComment}
              />
            </td>
          ) : (
            <div className=""></div>
          )}
        </td>
        <td className="comment-body comment-cell" style={{ width: "65%" }}>
          <div
            dangerouslySetInnerHTML={{
              __html: theseComments[comment].comment_body,
            }}
          />
        </td>
      </tr>
      {editForm ? (
        <EditComment
          commentId={theseComments[comment].id}
          setEditForm={setEditForm}
        />
      ) : (
        <></>
      )}
    </>
  );
};

export default DisplayComments;
