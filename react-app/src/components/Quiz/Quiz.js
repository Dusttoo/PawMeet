import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import {allBreedTraits} from '../../store/breed_traits'
import './Quiz.css'
import { useParams } from 'react-router';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import DisplayQuestion from './DisplayQuestion';
import UserResults from './QuizResults';


const Quiz = () => {
    const dispatch = useDispatch()
    const breedTraits = useSelector(state => state?.breed_traits)
    const [next, setNext] = useState(1)
    const userAnswers = useSelector(state => state.user_answers)
    const currentUser = useSelector(state => state.session.user)

    useEffect(() => {
        dispatch(allBreedTraits())
    },[dispatch])


    const alreadyTaken = Object.values(userAnswers).find((answer) => +answer.user_id === +currentUser.id)

    return (
        <>
            <h1>Quiz</h1>
            {alreadyTaken ? <UserResults /> : 
            
            <>
            {next < 17 ? 
             <DisplayQuestion trait={breedTraits[next]} next={setNext}/>
                : <UserResults />
            }
            </>}
            

            
            
        </>
    )}

export default Quiz