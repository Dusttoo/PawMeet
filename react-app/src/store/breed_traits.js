const GET_ALL_TRAITS = 'forum/GET_TRAITS'

const getAllTraits = (traits) => ({
    type: GET_ALL_TRAITS,
    traits
})

const initialState = {}

export const allBreedTraits = () => async (dispatch) => {
    const response = await fetch('/api/breeds/traits', {
        headers: {
            'Content-Type': 'application/json'
        }
        
    });
    const traits = await response.json();
    dispatch(getAllTraits(traits))
    return traits
}

export default function breedTraitReducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_TRAITS:
            const allTraits = {...state}
            action.traits.traits.forEach(trait => {
                allTraits[trait.id] = trait
            })
            return {...allTraits}
        default:
            return state;
    }
}