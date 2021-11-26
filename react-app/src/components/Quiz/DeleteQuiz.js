import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {removeAnswer, removeQuiz} from '../../store/user_answers'
import { useHistory } from 'react-router';
import './Quiz.css'


const DeleteQuiz = ({userId}) => {
    const dispatch = useDispatch()
    const history = useHistory()

    const deleteQuiz = () => {
        dispatch(removeAnswer(userId));
            history.push(`/breed-quiz/${userId}`)
    }


    return (
        <>
            <button className='delete-quiz' onClick={deleteQuiz}>
                Start over
            </button>
        </>
    )
}

export default DeleteQuiz