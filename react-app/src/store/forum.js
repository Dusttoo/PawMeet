const GET_ALL_POSTS = 'forum/GET_POSTS'
const GET_ALL_COMMENTS = 'forum/GET_COMMENT'

const getAllPosts = (posts) => ({
    type: GET_ALL_POSTS,
    posts
})

const getAllComments = (comments) => ({
    type: GET_ALL_COMMENTS,
    comments
})

const initialState = {}

export const allPosts = () => async (dispatch) => {
    const response = await fetch('/api/forum/posts', {
        headers: {
            'Content-Type': 'application/json'
        }
        
    });

    const posts = await response.json();
    dispatch(getAllPosts(posts))
    return posts
}

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

export default function forumReducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_POSTS:
            const allPosts = {...state}
            action.posts.posts.forEach(post => {
                allPosts[post.id] = post
            })
            return {...allPosts}
        case GET_ALL_COMMENTS:
            const allComments = {...state}
            action.comments.comments.forEach(comment => {
                allComments[comment.id] = comment
            })
            return {...allComments}
        default:
            return state;
    }
}


