const GET_ALL_POSTS = 'forum/GET_POSTS'

const getAllPosts = (posts) => ({
    type: GET_ALL_POSTS,
    posts
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

export default function forumReducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_POSTS:
            const allPosts = {...state}
            action.posts.posts.forEach(post => {
                allPosts[post.id] = post
            })
            return {...allPosts}
        default:
            return state;
    }
}


