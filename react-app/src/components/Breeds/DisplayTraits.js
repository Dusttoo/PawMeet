import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link, useParams } from 'react-router-dom';
import { allPets, removePet } from '../../store/pets';
import { useHistory } from 'react-router';
import { Carousel } from 'react-carousel-minimal';
import './Breed.css'
import { allBreedAnswers } from '../../store/breed_answers';
import { allBreedTraits } from '../../store/breed_traits';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faAngleDown, faAnglesDown } from '@fortawesome/free-solid-svg-icons';




const DisplayTraits = ({trait, thisAnswer}) => {
  const [details, setDetails] = useState(false)
  const openDetails = () => {
    if (details) {
      setDetails(false)
    } else {
      setDetails(true)
    }
  }



    return (
        <>
              <div className='trait-dropdown'>
                <h2 className='trait-header'>{trait.trait}</h2>
                <FontAwesomeIcon icon={faAngleDown}
                onClick={openDetails} />
              </div>
              {details ? 
              <p className='trait-description'>{trait.description}</p> : <></> }
              {thisAnswer.trait_id === 7 ? <></> :
              <div className='scale'>
                  <p className='least'>Least</p>
                  <p className='most'>Most</p>
              </div>
              }
              
              <div className="star-rating">
              {thisAnswer.trait_id === 7 || thisAnswer.trait_id === 8 ?
              <></> :
              [...Array(5)].map((star, rate) => {
              rate += 1;
              return (
                <>
                  <div className='breed-ratings'>
                    <button
                      type="button"
                      key={rate}
                      className={rate <= thisAnswer.answer ? "on" : "off"}
                    >
                      <span className="bubble"></span>
                    </button>
                  </div>
              </>
              );
            })}
              {thisAnswer.trait_id === 8 ?
              [...Array(3)].map((star, rate) => {
              rate += 1;
              const coatLengths = ['', 'Short', 'Medium', 'Long']
              return (
                <button
                  type="button"
                  key={rate}
                  className={rate === thisAnswer.answer ? "on" : "off"}
                >
                  <span className="bubble">{coatLengths[rate]}</span>
                </button>
              );
            }) : null}
            
              {thisAnswer.trait_id === 7 ? 
              <div className='coat-types'>
                {[...Array(9)].map((star, rate) => {
                rate += 1;
                const coatTypes = ['', 'Wiry', 'Rough', 'Curly', 'Hairless', 'Corded', 'Wavy', 'Smooth', 'Double', 'Silky']
                return (
                  <button
                    type="button"
                    key={rate}
                    className={rate === thisAnswer.answer ? "coatOn" : "coatOff"}
                  >
                    <span className="bubble">{coatTypes[rate]}</span>
                  </button>
                
              );
             
            })} 
            </div> : <></>}
            
            
            
          </div>
        </>
    )
}

export default DisplayTraits