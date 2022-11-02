import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { allPosts, removePost } from "../../store/forum";
import { useSelector } from "react-redux";
import { useParams, useHistory } from "react-router";
import EditPost from "./EditPost";
import AddComment from "./AddComment";
import DisplayComments from "./DisplayComment";
import { postComments } from "../../store/post_comments";
import { Link } from "react-router-dom";
import { addALike, removeLike } from "../../store/likes";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHeart } from "@fortawesome/free-solid-svg-icons";
import { getLikes, sortedByTime } from "../utils/helperFunctions";
import {
  faPen,
  faMinusCircle,
  faPlus,
} from "@fortawesome/free-solid-svg-icons";
import "./Forum.css";

const Posts = () => {
  const { postId } = useParams();
  const [loaded, setLoaded] = useState(false);
  const history = useHistory();
  const dispatch = useDispatch();
  const currentUser = useSelector((state) => state.session.user);
  const posts = useSelector((state) => state.forum);
  const users = useSelector((state) => state.users);
  const likes = useSelector((state) => state.likes);
  const comments = useSelector((state) => state.post_comments);
  const [likeHover, setLikeHover] = useState(false);
  const author = Object.keys(users).find(
    (user) => +user === +posts[postId].user_id
  );
  const thisUser = useSelector((state) => state.session.user);
  const [editForm, setEditForm] = useState(false);
  const [commentForm, setCommentForm] = useState(false);
  const liked = Object.values(likes).map((like) => {
    if (+like.post_id === +postId) {
      if (+like.user_id === +currentUser.id) {
        return true;
      }
      return false;
    }
  });
  const likeList = Object.values(likes).filter(
    (like) => like.post_id === +postId
  );
  useEffect(() => {
    (async () => {
      await dispatch(allPosts());
      await dispatch(postComments(postId));
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  const openEditForm = () => {
    if (editForm) {
      setEditForm(false);
    } else {
      setEditForm(true);
    }
  };

  const deletePost = () => {
    dispatch(removePost(postId));
    history.push(`/forum`);
  };

  const openCommentForm = () => {
    if (commentForm) {
      setCommentForm(false);
    } else {
      setCommentForm(true);
      window.scrollTo({
        top: 3000,
        left: 100,
        behavior: "smooth",
      });
    }
  };

  const addLike = () => {
    const createdLike = {
      user_id: currentUser.id,
      post_id: postId,
    };
    dispatch(addALike(createdLike));
  };

  const deleteLike = () => {
    const likeId = Object.values(likes).find(
      (like) => +like.user_id === +currentUser.id
    );
    dispatch(removeLike(+likeId.id));
  };

  return (
    <>
      <div className="post-container">
        <div className="post">
          {thisUser.id === +author ? (
            <div className="post-user-options">
              <FontAwesomeIcon
                className="edit-button"
                onClick={openEditForm}
                icon={faPen}
              />
              <FontAwesomeIcon
                className="delete-button"
                onClick={deletePost}
                icon={faMinusCircle}
              />
            </div>
          ) : (
            <></>
          )}

          <div className="post-header">
            <div className="comment-info">
              <Link to={`/users/${author}`}>
                <img
                  className="profile-icon"
                  src={users[author].profile_img}
                  alt={users[author].first_name}
                />
              </Link>
              <div className="name-date">
                <Link className="author-name" to={`/users/${author}`}>
                  {users[author].first_name} {users[author].last_name}
                </Link>
              </div>
            </div>
            <div className="post-title-container">
              <h1 className="show-post-title">{posts[postId].title}</h1>
            </div>
          </div>
          <div className="post-body-container">
            <div
              dangerouslySetInnerHTML={{ __html: posts[postId].post_body }}
            ></div>
          </div>

          <div className="like-section">
            {!liked.includes(true) ? (
              <div className="likes-container">
                <FontAwesomeIcon
                  className="like-heart"
                  onClick={addLike}
                  icon={faHeart}
                  style={{ color: "#d3d3d3" }}
                />
                {getLikes(Object.values(likes), postId)}
              </div>
            ) : (
              <div className="likes-container">
                <FontAwesomeIcon
                  className="like-heart"
                  onClick={deleteLike}
                  icon={faHeart}
                  style={{ color: "#ff0808" }}
                />
                {getLikes(Object.values(likes), postId)}
              </div>
            )}

            {likeList.length && !likeHover ? (
              <span
                className="people-liked-header"
                onClick={() => setLikeHover(!likeHover)}
              >
                People who liked this{" "}
              </span>
            ) : (
              <div
                className={likeHover ? "people-liked-container" : "hide-like"}
                onClick={() => setLikeHover(!likeHover)}
              >
                {likeList.slice(0, 3).map((like) => (
                  <span>
                    <Link className="author-name" to={`/users/${like.user_id}`}>
                      {users[like.user_id].first_name}
                    </Link>
                  </span>
                ))}
                {likeList.length > 1 && (
                  <span>
                    {" "}
                    ...
                    <Link
                      className="author-name"
                      to={`/users/${likeList[likeList.length - 1].user_id}`}
                    >
                      {" "}
                      {
                        users[likeList[likeList.length - 1].user_id].first_name
                      }{" "}
                    </Link>
                  </span>
                )}
              </div>
            )}
          </div>

          {editForm ? <EditPost setEditForm={setEditForm} /> : <></>}
        </div>
      </div>
      <div className="comment-container">
        <div className="post">
          <div className="comment-options-container">
            <FontAwesomeIcon
              icon={faPlus}
              className="add-comment"
              onClick={openCommentForm}
            />
          </div>

          <table className="comments-table">
            {sortedByTime(Object.values(comments)).map((comment) => {
              return <DisplayComments commentId={comment.id} />;
            })}
          </table>
          {commentForm ? <AddComment setCommentForm={setCommentForm} /> : <></>}
        </div>
      </div>
    </>
  );
};

export default Posts;
