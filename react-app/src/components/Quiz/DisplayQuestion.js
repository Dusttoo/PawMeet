import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link, useHistory } from 'react-router-dom';
import './Quiz.css'
import { useParams } from 'react-router';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { addAnAnswer } from '../../store/user_answers';


const DisplayQuestion = ({trait, next}) => {
    const [validationErrors, setValidationErrors] = useState([]);
    const dispatch = useDispatch()
    const trait_id = trait.id
    const [answer, setAnswer] = useState('')
    // const [important, setImportant] = useState('')
    const user_id = useSelector(state => state.session.user.id)
    const history = useHistory();
    const normal = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 16]
    const coatTypes = ['Wiry', 'Rough', 'Curly', 'Hairless', 'Corded', 'Wavy', 'Smooth', 'Double', 'Silky']
    let index = 0;
    const coatLengths = ['Short', 'Medium', 'Long']

    const validate = () => {
        const validationErrors = [];

        return validationErrors;
    }

    const handleSubmit = async (e) => {
    e.preventDefault();
        const createdAnswer = {
          user_id,
          trait_id,
          answer: +answer,
        //   important
        };
        const errors = validate();

        console.log(createdAnswer)

        if (errors.length > 0) {
            setValidationErrors(errors);
        } else {
            setValidationErrors([]);
            const added = await dispatch(addAnAnswer(createdAnswer));
            if(added) {
              
            }
            
        };
    next(trait.id++)

}




    return (
        <>
        <h2 className='question'>{trait.question}</h2>
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
              <div className="add-form-con">
                    <div className='radio-container'>
                        {trait.id === 7 ?
                        
                        <>
                        {coatTypes.map((coat) => {
                            index++
                        return (
                        <div className='min-max'>
                            <label className='form-label'>{coat}
                            <input
                            type='radio'
                            name='type'
                            className="quiz-radio"
                            value={index}
                            onChange={(e) => setAnswer(e.target.value)}
                            required/></label>
                        </div>
                        )    
                        
                        })}
                        </>: <></>}

                        {trait.id === 8 ?
                        <>
                        {coatLengths.map((coat) => {
                        index++
                            return (
                            <div className='min-max'>
                                <label className='form-label'>{coat}
                                <input
                                type='radio'
                                name='length'
                                className="quiz-radio"
                                value={index}
                                onChange={(e) => setAnswer(e.target.value)}
                                required/></label>
                            </div>
                        )    
                        
                        })}
                        </>
                        : <></>}


                        {normal.includes(trait.id) ? 
                        <>
                        <div className='min-max'>
                            <label className='form-label'>{trait.min}</label>
                            <input
                            type='radio'
                            name='answer'
                            className="quiz-radio"
                            value={1}
                            onChange={(e) => setAnswer(e.target.value)}
                            required/>
                        </div>
                        <div className='min-max'>
                            <label className='form-label'></label>
                            <input
                            type='radio'
                            className="quiz-radio"
                            name='answer'
                            value={2}
                            onChange={(e) => setAnswer(e.target.value)}
                            required/>
                        </div>
                        <div className='min-max'>
                            <label className='form-label'></label>

                            <input
                            type='radio'
                            className="quiz-radio"
                            name='answer'
                            value={3}
                            onChange={(e) => setAnswer(e.target.value)}
                            required/>
                        </div>
                        <div className='min-max'>
                            <label className='form-label'></label>

                            <input
                            type='radio'
                            className="quiz-radio"
                            name='answer'
                            value={4}
                            onChange={(e) => setAnswer(e.target.value)}
                            required/>
                        </div>
                        <div className='min-max'>
                            <label className='form-label'>{trait.max}</label>
                            <input
                            type='radio'
                            className="quiz-radio"
                            name='answer'
                            value={5}
                            onChange={(e) => setAnswer(e.target.value)}
                            required/>
                        </div>
                        </>
                        :<></>}
                    </div>
                <div className='submit-container'><button className="form-button" type="submit">Next</button></div>
              </div>
            </form>
          </div>
            
        </>
    )
}

export default DisplayQuestion