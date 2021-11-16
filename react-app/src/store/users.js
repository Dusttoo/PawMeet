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
      console.log('users thunk', users)
      dispatch(getUsers(users));
      return users
}

export default function usersReducer(state = initialState, action) {
    switch (action.type) {
        case GET_USERS:
        console.log('action', action.users, action.users.users)
          const everyUser = {...state}
          action.users.users.forEach(user => {
            everyUser[user.id] = user
          })
          console.log('all users', everyUser)
          return {...everyUser}
        default:
            return state;

    }
}