const GET_ALL_REQUESTS = "friends/GET_REQUESTS";
const GET_ALL_FRIENDS  = 'friends/GET_FRIENDS';

const getAllRequests = (requests) => ({
  type: GET_ALL_REQUESTS,
  requests,
});

const getAllFriends = (friends) => ({
  type: GET_ALL_FRIENDS,
  friends,
});

const initialState = {requests: {}, list: {}};

export const allRequests = (userId) => async (dispatch) => {
  const response = await fetch(`/api/friends/${userId}/requests`, {
    headers: {
      "Content-Type": "application/json",
    },
  });
  const request = await response.json();
  dispatch(getAllRequests(request));
  return request;
};

export const allFriends = (userId) => async (dispatch) => {
  const response = await fetch(`/api/friends/${userId}/friends`, {
    headers: {
      "Content-Type": "application/json",
    },
  });
  const request = await response.json();
  dispatch(getAllFriends(request));
  return request;
};

export default function friendReducer(state = initialState, action) {
  switch (action.type) {
    case GET_ALL_REQUESTS:
      const allrequests = { ...state };
      action.requests.requests.forEach((request) => {
        allrequests.requests[request.id] = request;
      });
      return { ...allrequests };
    case GET_ALL_FRIENDS:
      const allfriends = { ...state };
      action.friends.friends.forEach((friend) => {
        allfriends.list[friend.id] = friend;
      });
      return { ...allfriends };
    default:
      return state;
  }
}
