const GET_ALL_POSTS = 'forum/GET_POSTS'
const ADD_POST = 'forum/ADD_POST'
const UPDATE_POST = 'forum/UPDATE_POST'

const getAllPosts = (posts) => ({
    type: GET_ALL_POSTS,
    posts
})

const addPost = (post) => ({
    type: ADD_POST,
    post
})

const upadtePost = (post) => ({
    type: UPDATE_POST,
    post
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

export const addAPost = (post) => async(dispatch) => {
    const response = await fetch(`/api/forum/posts/add`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(post)
    });
    const added = await response.json();
    dispatch(addPost(added))
    return added
}

export const editAPost = (post, postId) => async(dispatch) => {
    const response = await fetch(`/api/forum/posts/${postId}/edit`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(post)
    });
    const added = await response.json();
    dispatch(upadtePost(added))
    return added
}

export default function forumReducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_POSTS:
            const allPosts = {...state}
            action.posts.posts.forEach(post => {
                allPosts[post.id] = post
            })
            return {...allPosts}
        case ADD_POST:
          const newState = {...state}
            newState[action.post.id] = action.post
            return newState
        case UPDATE_POST:
            const updatePost = {...state}
            updatePost[action.post.id] = action.post
            return {...updatePost}

        default:
            return state;
    }
}


