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
import Loading from '../Loading/Loading';
import {allUserAnswers} from '../../store/user_answers'




const Quiz = () => {
    const dispatch = useDispatch()
    const breedTraits = useSelector(state => state?.breed_traits)
    const userAnswers = useSelector(state => state.user_answers)
    const currentUser = useSelector(state => state.session.user)
    const [loading, setLoading] = useState(false)
    



    useEffect(() => {
        dispatch(allBreedTraits())
        dispatch(allUserAnswers(currentUser.id))
        // setLoading(false);

    },[dispatch])



    return (
        <div className='quiz-container'>
        {loading ? 
        <>
        <Loading />
        
        </> :
        <>
            {Object.keys(userAnswers).length >= 16 ? 
            <>
            <div className='results-page-container'>
                <h1 className='matches-title'>Your Matches</h1>
                <UserResults /> 
            </div>
            </>: 
            
            <>
             <DisplayQuestion />
            </>}
        </>}
            

            
            
        </div>
    )}

export default Quiz