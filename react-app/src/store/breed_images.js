const GET_ALL_IMAGES = 'forum/GET_IMAGES'

const getAllImages = (images) => ({
    type: GET_ALL_IMAGES,
    images
})

const initialState = {}

export const allImages = () => async (dispatch) => {
    const response = await fetch('/api/breeds/images', {
        headers: {
            'Content-Type': 'application/json'
        }
        
    });
    const images = await response.json();
    dispatch(getAllImages(images))
    return images
}

export default function imageReducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_IMAGES:
            const allImages = {...state}
            action.images.images.forEach(image => {
                allImages[image.id] = image
            })
            return {...allImages}
        default:
            return state;
    }
}