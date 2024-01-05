const GET_ALL_LIKES = "forum/GET_LIKES";
const ADD_LIKE = "forum/ADD_LIKE";
const DELETE_LIKE = "forum/DELETE_LIKE";

const getAllLikes = (likes) => ({
  type: GET_ALL_LIKES,
  likes,
});

const addLike = (like) => ({
  type: ADD_LIKE,
  like,
});

const deleteLike = (likeId) => ({
  type: DELETE_LIKE,
  likeId,
});

const initialState = {};

export const allLikes = () => async (dispatch) => {
  const response = await fetch("/api/forum/likes", {
    headers: {
      "Content-Type": "application/json",
    },
  });

  const likes = await response.json();
  dispatch(getAllLikes(likes));
  return likes;
};

export const addALike = (like) => async (dispatch) => {
  const response = await fetch(`/api/forum/likes/add`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(like),
  });
  const added = await response.json();
  dispatch(addLike(added));
  return added;
};

export const removeLike = (likeId) => async (dispatch) => {
  const response = await fetch(`/api/forum/likes/${likeId}/delete`, {
    method: "DELETE",
    statusCode: 204,
    headers: { "Content-Type": "application/json" },
  });

  if (response.ok) {
    const like = await response.json();
    dispatch(deleteLike(likeId));
  }
  return likeId;
};

export default function likeReducer(state = initialState, action) {
  switch (action.type) {
    case GET_ALL_LIKES:
      const allLikes = { ...state };
      action.likes.likes.forEach((like) => {
        allLikes[like.id] = like;
      });
      return { ...allLikes };
    case ADD_LIKE:
      const newState = { ...state };
      newState[action.like.id] = action.like;
      return newState;
    case DELETE_LIKE:
      const deleteState = { ...state };
      delete deleteState[action.likeId];
      return deleteState;
    default:
      return state;
  }
}
