const GET_USER_ANSWERS = 'forum/GET_ANSWERS'

const getAllUserAnswers = (answers) => ({
    type: GET_USER_ANSWERS,
    answers
})

const initialState = {}

export const allUserAnswers = (id) => async (dispatch) => {
    const response = await fetch(`/api/quiz/${id}`, {
        headers: {
            'Content-Type': 'application/json'
        }
        
    });
    const answers = await response.json();
    dispatch(getAllUserAnswers(answers))

    return answers
}

export default function userAnswerReducer(state = initialState, action) {
    switch (action.type) {
        case GET_USER_ANSWERS:
            const allAnswers = {}
            action.answers.answers.forEach(answer => {
                allAnswers[answer.id] = answer
            })
            return {...allAnswers}
        default:
            return state;
    }
}