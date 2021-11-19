const GET_ALL_PETS = 'forum/GET_PETS'
const ADD_PET = 'forum/ADD_PET'
const UPDATE_PET = 'forum/UPDATE_PET'
const DELETE_PET = 'forum/DELETE_PET'


const getAllPets = (pets) => ({
    type: GET_ALL_PETS,
    pets
})

const addPet = (pet) => ({
    type: ADD_PET,
    pet
})

const upadtePet = (pet) => ({
    type: UPDATE_PET,
    pet
})

const deletePost = (petId) => ({
    type: DELETE_PET,
    petId
})


const initialState = {}

export const allPets = () => async (dispatch) => {
    const response = await fetch('/api/pets', {
        headers: {
            'Content-Type': 'application/json'
        }
        
    });
    const pets = await response.json();
    dispatch(getAllPets(pets))
    return pets
}

export const addAPet = (pet) => async(dispatch) => {
    console.log(pet)
    const response = await fetch(`/api/pets/add`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(pet)
    });
    const added = await response.json();
    dispatch(addPet(added))
    return added
}

export const editAPet = (pet, petId) => async(dispatch) => {
    const response = await fetch(`/api/pets/${petId}/edit`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(pet)
    });
    const added = await response.json();
    dispatch(upadtePet(added))
    return added
}

export const removePet = (petId) => async (dispatch) => {
  
  const response = await fetch(`/api/pets/${petId}/delete`,{
  method: 'DELETE',
  statusCode: 204,
  headers: {'Content-Type': 'application/json'}
});

  if(response.ok) {
    const pet = await response.json();
    dispatch(deletePost(petId));
  }
    return petId


}

export default function petReducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_PETS:
            const allPets = {...state}
            action.pets.pets.forEach(pet => {
                allPets[pet.id] = pet
            })
            return {...allPets}
        case ADD_PET:
          const newState = {...state}
            newState[action.pet.id] = action.pet
            return newState
        case UPDATE_PET:
            const updatePet = {...state}
            updatePet[action.pet.id] = action.pet
            return {...updatePet}
        case DELETE_PET:
            const deleteState = {...state}
            delete deleteState[action.petId]
            return deleteState
        default:
            return state;
    }
}