const GET_POSTS_FOR_GROUP = 'forum/GET_POSTS_FOR_GROUP'
const getPostsForGroup = (posts) => ({
    type: GET_POSTS_FOR_GROUP,
    posts
})
const initialState = {}

export const allPostsForGroup = (id) => async (dispatch) => {
    const response = await fetch(`/api/forum/posts/${id}`, {
        headers: {
            'Content-Type': 'application/json'
        }
        
    });
    const posts = await response.json();
    console.log('response posts' , posts)
    dispatch(getPostsForGroup(posts))
    return posts
}

export default function groupPostReducer(state = initialState, action) {
    switch (action.type) {
        case GET_POSTS_FOR_GROUP:
            const allGroupPosts = {...state}
            action.posts.posts.forEach(post => {
                allGroupPosts[post.id] = post
            })
            return {...allGroupPosts}

        default:
            return state;
    }
}
