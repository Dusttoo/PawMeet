const GET_ALL_MESSAGES = "forum/GET_MESSAGES";
const ADD_MESSAGE = "forum/ADD_MESSAGE";
const DELETE_MESSAGE = "forum/DELETE_MESSAGE";

const getAllMessages = (messages) => ({
  type: GET_ALL_MESSAGES,
  messages,
});

const addMessage = (message) => ({
  type: ADD_MESSAGE,
  message,
});

const deleteMessage = (messageId) => ({
  type: DELETE_MESSAGE,
  messageId,
});

const initialState = {};

export const allMessages = (id) => async (dispatch) => {
  const response = await fetch(`/api/sockets/http-call/${id}`, {
    headers: {
      "Content-Type": "application/json",
    },
  });

  const message = await response.json();
  dispatch(getAllMessages(message));
  return message;
};

export const addAMessage= (message) => async (dispatch) => {
  const response = await fetch(`/api/socket/http-call/add`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(message),
  });
  const added = await response.json();
  dispatch(addMessage(added));
  return added;
};

export const removeMessage = (MessageId) => async (dispatch) => {
  const response = await fetch(`/api/socket/http-call/${MessageId}/delete`, {
    method: "DELETE",
    statusCode: 204,
    headers: { "Content-Type": "application/json" },
  });

  if (response.ok) {
    const message = await response.json();
    dispatch(deleteMessage(MessageId));
  }
  return MessageId;
};

export default function messageReducer(state = initialState, action) {
  switch (action.type) {
    case GET_ALL_MESSAGES:
      const allMessages = { ...state };
      action.messages.messages.forEach((message) => {
        allMessages[message.id] = message;
      });
      return { ...allMessages };
    case ADD_MESSAGE:
      const newState = { ...state };
      newState[action.message.id] = action.message;
      return newState;
    case DELETE_MESSAGE:
      const deleteState = { ...state };
      delete deleteState[action.MessageId];
      return deleteState;
    default:
      return state;
  }
}
