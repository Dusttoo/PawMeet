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
import GifPlayer from 'react-gif-player'



const Quiz = () => {
    const dispatch = useDispatch()
    const breedTraits = useSelector(state => state?.breed_traits)
    const userAnswers = useSelector(state => state.user_answers)
    const currentUser = useSelector(state => state.session.user)
    // const [loading, setLoading] = useState(false)
    



    useEffect(() => {
        dispatch(allBreedTraits())
    },[dispatch])


    const alreadyTaken = Object.values(userAnswers).filter((answer) => +answer.user_id === +currentUser.id)
    console.log(alreadyTaken.length)

    return (
        <>
            <h1>Quiz</h1>
            {alreadyTaken.length === 16 ? <UserResults /> : 
            
            <>
             <DisplayQuestion />
            </>}
            

            
            
        </>
    )}

export default Quiz