const GET_POST_COMMENTS = 'forum/GET_POST_COMMENTS'
const ADD_POST_COMMENT = 'forum/ADD_POST_COMMENT'
const UPDATE_COMMENT = 'forum/UPDATE_COMMENT'
const DELETE_COMMENT = 'forum/DELETE_COMMENT'


const getPostComments = (comments) => ({
    type: GET_POST_COMMENTS,
    comments
})

const addComment = (comment) => ({
    type: ADD_POST_COMMENT,
    comment
})

const upadteComment = (comment) => ({
    type: UPDATE_COMMENT,
    comment
})

const deleteComment = (commentId) => ({
    type: DELETE_COMMENT,
    commentId
})

export const postComments = (postId) => async (dispatch) => {
    const response = await fetch(`/api/forum/posts/${postId}/comments`, {
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const comments = await response.json();
    dispatch(getPostComments(comments))
    return comments
}

export const addAComment = (comment) => async(dispatch) => {
    const response = await fetch(`/api/forum/comments/add`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(comment)
    });
    const added = await response.json();
    dispatch(addComment(added))
    return added
}

export const editAComment = (comment, commentId) => async(dispatch) => {
    const response = await fetch(`/api/forum/comments/${commentId}/edit`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(comment)
    });
    const added = await response.json();
    dispatch(upadteComment(added))
    return added
}

export const removeComment = (commentId) => async (dispatch) => {
  const response = await fetch(`/api/forum/comments/${commentId}/delete`,{
  method: 'DELETE',
  statusCode: 204,
  headers: {'Content-Type': 'application/json'}
});

  if(response.ok) {
    const comment = await response.json();
    dispatch(deleteComment(commentId));
  }
    return commentId


}


const initialState = {}

export default function post_commentReducer(state = initialState, action) {
    switch(action.type) {
        case GET_POST_COMMENTS:
            const postComments = {}
            action.comments.comments.forEach(comment => {
                postComments[comment.id] = comment
            })
            console.log(postComments)
            return {...postComments}
        case ADD_POST_COMMENT:
          const newState = {...state}
            newState[action.comment.id] = action.comment
            console.log(newState, 'new state for add comment')
            return newState
        case UPDATE_COMMENT:
            const updateComment = {...state}
            updateComment[action.comment.id] = action.comment
            return {...updateComment}
        case DELETE_COMMENT:
            const deleteState = {...state}
            delete deleteState[action.commentId]
            return deleteState
        default:
            return state

    }
}