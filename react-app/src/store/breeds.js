const GET_ALL_BREEDS = 'forum/GET_BREEDS'

const getAllBreeds = (breeds) => ({
    type: GET_ALL_BREEDS,
    breeds
})

const initialState = {}

export const allBreeds = () => async (dispatch) => {
    const response = await fetch('/api/breeds', {
        headers: {
            'Content-Type': 'application/json'
        }
        
    });
    const breeds = await response.json();
    dispatch(getAllBreeds(breeds))
    return breeds
}

export default function breedReducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_BREEDS:
            const allBreeds = {...state}
            action.breeds.breeds.forEach(breed => {
                allBreeds[breed.id] = breed
            })
            return {...allBreeds}
        default:
            return state;
    }
}
