const GET_ALL_ANSWERS = "forum/GET_ANSWERS";

const getAllAnswers = (answers) => ({
  type: GET_ALL_ANSWERS,
  answers,
});

const initialState = {};

export const allBreedAnswers = () => async (dispatch) => {
  const response = await fetch("/api/breeds/answers", {
    headers: {
      "Content-Type": "application/json",
    },
  });
  const answers = await response.json();
  dispatch(getAllAnswers(answers));

  return answers;
};

export default function breedAnswerReducer(state = initialState, action) {
  switch (action.type) {
    case GET_ALL_ANSWERS:
      const allAnswers = { ...state };

      action.answers.answers.forEach((answer) => {
        allAnswers[answer.id] = answer;
      });
      return { ...allAnswers };
    default:
      return state;
  }
}
