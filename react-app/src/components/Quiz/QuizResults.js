import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import './Quiz.css'
import { allUsers } from '../../store/users';
import { useParams } from 'react-router';
import { allUserAnswers } from '../../store/user_answers';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAngleLeft, faAngleRight } from '@fortawesome/free-solid-svg-icons';
import { allBreedAnswers } from '../../store/breed_answers';



const UserResults = () => {
    const {id} = useParams()
    const dispatch = useDispatch()
    const breeds = useSelector(state => state.breeds)
    const breedAnswers = useSelector(state => state.breed_answers)
    const userAnswers = useSelector(state => state.user_answers)
    const images = useSelector(state => state.breed_images)
    let index = 0;
    const results = []


    useEffect(() => {
      dispatch(allUserAnswers(id))
      dispatch(allBreedAnswers())
  }, [dispatch, id]);

  const calculateResults = () => {
    Object.values(breeds).map((breed) => {
        let total = 0;
        let average = 0;
        const breedResponses = Object.values(breedAnswers).filter(answer => 
            +answer.breed_id === +breed.id)
        const userResponses = Object.values(userAnswers)
        
        for(let i = 0; i < breedResponses.length; i++) {
            if(breedResponses[i].answer === userResponses[i].answer) {
                total++
            }
        }
        
        average = (total / breedResponses.length) * 100
        results.push([breed.id, average])

    })
  }

  calculateResults()
  const sortedResults = results.sort(function(a, b){return b[1]-a[1]})

  const topResults = () => {
      const top = []
      for (let i = 0; i < 5; i++) {
        top.push(results[i])
      }
      return top
  }


    return (
        <>
            {topResults().map((breed) => {
                const thisBreed= breeds[breed[0]]
                const thisImage = Object.values(images).find((image) => image.breed_id === thisBreed.id)
                return (
                <div className='breed-results-container'>
                  <img className='breed-link-image' src={thisImage.img_url} alt={thisBreed.name}/>
                  <Link className='breed' to={`/breeds/${thisBreed.id}`}>{thisBreed.name} {breed[1]}% match</Link>
                </div>
                )
            })}
        </>
    )
}

export default UserResults