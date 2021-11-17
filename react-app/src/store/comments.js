const GET_ALL_COMMENTS = 'forum/GET_COMMENT'

const getAllComments = (comments) => ({
    type: GET_ALL_COMMENTS,
    comments
})

const initialState = {}

export const allComments = () => async (dispatch) => {
    const response = await fetch('/api/forum/comments', {
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const comments = await response.json();
    dispatch(getAllComments(comments))
    return comments
}

export default function commentReducer(state = initialState, action) {
    switch(action.type) {
        case GET_ALL_COMMENTS:
            const allComments = {...state}
            action.comments.comments.forEach(comment => {
                allComments[comment.id] = comment
            })
            return {...allComments}
        default:
            return state

    }
}