const GET_ALL_COMMENTS = "forum/GET_COMMENT";
const ADD_COMMENT = "forum/ADD_COMMENT";
const UPDATE_COMMENT = "forum/UPDATE_COMMENT";
const DELETE_COMMENT = "forum/DELETE_COMMENT";

const getAllComments = (comments) => ({
  type: GET_ALL_COMMENTS,
  comments,
});

const addComment = (comment) => ({
  type: ADD_COMMENT,
  comment,
});

const upadteComment = (comment) => ({
  type: UPDATE_COMMENT,
  comment,
});

const deleteComment = (commentId) => ({
  type: DELETE_COMMENT,
  commentId,
});

const initialState = {};

export const allComments = () => async (dispatch) => {
  const response = await fetch("/api/forum/comments", {
    headers: {
      "Content-Type": "application/json",
    },
  });

  const comments = await response.json();
  dispatch(getAllComments(comments));
  return comments;
};

export const addAComment = (comment) => async (dispatch) => {
  const response = await fetch(`/api/forum/comments/add`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(comment),
  });
  const added = await response.json();
  dispatch(addComment(added));
  return added;
};

export const editAComment = (comment, commentId) => async (dispatch) => {
  const response = await fetch(`/api/forum/comments/${commentId}/edit`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(comment),
  });
  const added = await response.json();
  dispatch(upadteComment(added));
  return added;
};

export const removeComment = (commentId) => async (dispatch) => {
  const response = await fetch(`/api/forum/comments/${commentId}/delete`, {
    method: "DELETE",
    statusCode: 204,
    headers: { "Content-Type": "application/json" },
  });

  if (response.ok) {
    const comment = await response.json();
    dispatch(deleteComment(commentId));
  }
  return commentId;
};

export default function commentReducer(state = initialState, action) {
  switch (action.type) {
    case GET_ALL_COMMENTS:
      const allComments = { ...state };
      action.comments.comments.forEach((comment) => {
        allComments[comment.id] = comment;
      });
      return { ...allComments };
    case ADD_COMMENT:
      const newState = { ...state };
      newState[action.comment.id] = action.comment;
      return newState;
    case UPDATE_COMMENT:
      const updateComment = { ...state };
      updateComment[action.comment.id] = action.comment;
      return { ...updateComment };
    case DELETE_COMMENT:
      const deleteState = { ...state };
      delete deleteState[action.commentId];
      return deleteState;
    default:
      return state;
  }
}
