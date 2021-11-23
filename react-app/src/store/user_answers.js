const GET_USER_ANSWERS = 'quiz/GET_ANSWERS'
const ADD_ANSWER = 'quiz/ADD_ANSWER'

const getAllUserAnswers = (answers) => ({
    type: GET_USER_ANSWERS,
    answers
})

const addAnswer = (answer) => ({
    type: ADD_ANSWER,
    answer
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

export const addAnAnswer = (answer) => async(dispatch) => {
    const response = await fetch(`/api/quiz/add`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(answer)
    });
    const added = await response.json();
    dispatch(addAnswer(added))
    return added
}

export default function userAnswerReducer(state = initialState, action) {
    switch (action.type) {
        case GET_USER_ANSWERS:
            const allAnswers = {}
            action.answers.answers.forEach(answer => {
                allAnswers[answer.id] = answer
            })
            return {...allAnswers}
        case ADD_ANSWER:
          const newState = {...state}
            newState[action.answer.id] = action.answer
            return newState
        default:
            return state;
    }
}