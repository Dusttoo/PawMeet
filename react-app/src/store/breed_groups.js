const GET_ALL_GROUPS = "forum/GET_GROUPS";

const getAllGroups = (groups) => ({
  type: GET_ALL_GROUPS,
  groups,
});

const initialState = {};

export const allGroups = () => async (dispatch) => {
  const response = await fetch("/api/breeds/groups", {
    headers: {
      "Content-Type": "application/json",
    },
  });
  const groups = await response.json();
  dispatch(getAllGroups(groups));
  return groups;
};

export default function groupReducer(state = initialState, action) {
  switch (action.type) {
    case GET_ALL_GROUPS:
      const allGroups = { ...state };
      action.groups.groups.forEach((group) => {
        allGroups[group.id] = group;
      });
      return { ...allGroups };
    default:
      return state;
  }
}
