const GET_ALL_REQUESTS = "forum/GET_REQUESTS";

const getAllRequests = (requests) => ({
  type: GET_ALL_REQUESTS,
  requests,
});

const initialState = {requests: {}, list: {}};

export const allRequests = (userId) => async (dispatch) => {
    console.log('dispatched')
  const response = await fetch(`/api/friends/${userId}/requests`, {
    headers: {
      "Content-Type": "application/json",
    },
  });
  const request = await response.json();
  dispatch(getAllRequests(request));
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
    default:
      return state;
  }
}
