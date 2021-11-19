const GET_USERS = 'session/GET_USERS'

const getUsers = (users) => ({
  type: GET_USERS,
  users
})

const initialState = {};

export const allUsers = () => async (dispatch) => {
  const response = await fetch('/api/users/', {
    headers: {
      'Content-Type': 'application/json'
    }
  });
      const users = await response.json();
      dispatch(getUsers(users));
      return users
}

export default function usersReducer(state = initialState, action) {
    switch (action.type) {
        case GET_USERS:
          const everyUser = {...state}
          action.users.users.forEach(user => {
            everyUser[user.id] = user
          })
          return {...everyUser}
        default:
            return state;

    }
}