const GET_POST_COMMENTS = 'forum/GET_POST_COMMENTS'

const getPostComments = (comments) => ({
    type: GET_POST_COMMENTS,
    comments
})

export const postComments = (postId) => async (dispatch) => {
    const response = await fetch(`/api/forum/posts/${postId}/comments`, {
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const comments = await response.json();
    console.log('RESPONSE', comments)
    dispatch(getPostComments(comments))
    return comments
}
const initialState = {}

export default function post_commentReducer(state = initialState, action) {
    switch(action.type) {
        case GET_POST_COMMENTS:
            const postComments = {}
            console.log('pre-state', postComments)
            action.comments.comments.forEach(comment => {
                postComments[comment.id] = comment
            })
            console.log('return state', postComments)
            return {...postComments}
        default:
            return state

    }
}