import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link, useHistory } from 'react-router-dom';
import './Quiz.css'
import { useParams } from 'react-router';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faRightLong } from '@fortawesome/free-solid-svg-icons';
import { addAnAnswer } from '../../store/user_answers';
import GifPlayer from 'react-gif-player'


const DisplayQuestion = () => {
    const [validationErrors, setValidationErrors] = useState([]);
    const dispatch = useDispatch()
    const [answer, setAnswer] = useState('')
    const [next, setNext] = useState(1)
    const breedTraits = useSelector(state => state?.breed_traits)
    const trait_id = breedTraits[next].id
    const breeds = useSelector(state => state?.breeds)
    // const [important, setImportant] = useState('')
    const user_id = useSelector(state => state.session.user.id)
    const history = useHistory();
    const normal = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 16]
    const coatTypes = ['Wiry', 'Rough', 'Curly', 'Hairless', 'Corded', 'Wavy', 'Smooth', 'Double', 'Silky']
    let index = 0;
    const coatLengths = ['Short', 'Medium', 'Long']
    const breedImages = useSelector(state => state.breed_images)
    const [loading, setLoading] = useState(false)
    const [img, setImg] = useState('https://images.pexels.com/photos/162149/dog-black-labrador-black-dog-162149.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260')
    console.log('image', img)

    
    const imageSet = () => {
        const num = Math.floor(Math.random() * Object.keys(breeds).length - 1)
        console.log('num', num)
         setImg(Object.values(breedImages)[num].img_url)
    }

    const validate = () => {
        const validationErrors = [];

        return validationErrors;
    }

    const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true)


        const createdAnswer = {
          user_id,
          trait_id,
          answer: +answer,
        //   important
        };
        const errors = validate();


        if (errors.length > 0) {
            setValidationErrors(errors);
        } else {
            setValidationErrors([]);
            const added = await dispatch(addAnAnswer(createdAnswer));
            if(added) {
              
            }
            
        };
        
        setNext(next + 1)
        imageSet()
        setLoading(false)


}







    return (
        <div className='question-quiz-container'>
        {loading ? 
        <>
        <div className='loading-container'>
            <GifPlayer gif="https://i.imgur.com/JS8bT2R.gif" autoplay={true} />
            <h2 className='highlighted-breed-name'>Calling all the dogs...</h2>
        </div>
        </> :
        <>
        <div className='image-container'>
            <img className='quiz-image' src={img} alt='breed quiz'></img>
            <h2 className='question'>{breedTraits[next].question}</h2>
        </div>
        {validationErrors.length > 0 && (
        <div className="errors">
            <p className="error-title"> The following errors were found: </p>
            <ul className="error-list">
                {validationErrors.map(error => <li className="error" key={error}>{error}</li>)}
            </ul>
        </div>
        )}
        
        <div className="add-form-container">
            <form className='post-form' onSubmit={handleSubmit}>
              <div className="quiz-form-con">
                    <div className='coat-container'>
                        {breedTraits[next].id === 7 ?
                        
                        <>
                        {coatTypes.map((coat) => {
                            index++
                        return (
                        <div className='coat-min-max'>
                            <label className='coat-radio-title'>{coat}</label>
                            <label className='container'>
                                <input
                                type='radio'
                                name='type'
                                className="quiz-radio"
                                value={index}
                                onChange={(e) => setAnswer(e.target.value)}
                                required/>
                                <span className='checkmark'></span>
                            </label>
                        </div>
                        )    
                        
                        })}
                        </>: <></>}

                        {breedTraits[next].id === 8 ?
                        <>
                        {coatLengths.map((coat) => {
                        index++
                            return (
                            <div className='coat-min-max'>
                                <label className='coat-radio-title'>{coat}</label>
                                <label className='container'>
                                    <input
                                    type='radio'
                                    name='length'
                                    className="quiz-radio"
                                    value={index}
                                    onChange={(e) => setAnswer(e.target.value)}
                                    required/>
                                    <span className='checkmark'></span>
                                </label>
                            </div>
                        )    
                        
                        })}
                        </>
                        : <></>}


                        {normal.includes(breedTraits[next].id) ? 
                        <>
                        <div className='min-max'>
                            <label className='radio-title'>{breedTraits[next].min}</label>
                            <label className='container'>
                                <input
                                type='radio'
                                name='answer'
                                className="quiz-radio"
                                value={1}
                                onChange={(e) => setAnswer(e.target.value)}
                                required/>
                                <span className='checkmark'></span>
                            </label>

                        </div>
                        <div className='min-max'>
                            <label className='container'>
                                <input
                                type='radio'
                                className="quiz-radio"
                                name='answer'
                                value={2}
                                onChange={(e) => setAnswer(e.target.value)}
                                required/>
                                <span className='checkmark'></span>
                            </label>

                        </div>
                        <div className='min-max'>
                            <label className='container'>

                                <input
                                type='radio'
                                className="quiz-radio"
                                name='answer'
                                value={3}
                                onChange={(e) => setAnswer(e.target.value)}
                                required/>
                                <span className='checkmark'></span>
                            </label>

                        </div>
                        <div className='min-max'>
                            <label className='container'>

                                <input
                                type='radio'
                                className="quiz-radio"
                                name='answer'
                                value={4}
                                onChange={(e) => setAnswer(e.target.value)}
                                required/>
                                <span className='checkmark'></span>
                            </label>

                        </div>
                        <div className='min-max'>
                            <label className='radio-title'>{breedTraits[next].max}</label>
                            <label className='container'>
                                <input
                                type='radio'
                                className="quiz-radio"
                                name='answer'
                                value={5}
                                onChange={(e) => setAnswer(e.target.value)}
                                required/>
                                <span className='checkmark'></span>
                            </label>

                        </div>
                        </>
                        :<></>}
                    </div>
                <div className='submit-container'><button className="quiz-button" type="submit">Next <FontAwesomeIcon className='arrow' icon={faRightLong}/></button></div>
              </div>
            </form>
          </div>
        </>}
            
        </div>
    )
}

export default DisplayQuestion