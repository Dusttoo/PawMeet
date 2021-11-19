import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link, useParams } from 'react-router-dom';
import { allPets, removePet } from '../../store/pets';
import { useHistory } from 'react-router';
import './Breed.css'
import { allBreedTraits } from '../../store/breed_traits';
import { allBreedAnswers } from '../../store/breed_answers';



const BreedsPage = () => {
    const breeds = useSelector(state => state.breeds)
    const images = useSelector(state => state.breed_images)
    const dispatch = useDispatch()
    const [loaded, setLoaded] = useState(false);


    useEffect(() => {
    (async() => {
      await dispatch(allBreedTraits())
      await dispatch(allBreedAnswers())
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }


    return (
        <>
          <div className='breed-list-container'>
            {Object.values(breeds).map((breed) => {
              const thisImage = Object.values(images).find((image) => image.breed_id === breed.id)
                return (
                <div className='breed-container'>
                  <img src={thisImage.img_url} alt={breed.name}/>
                  <Link className='breed' to={`/breeds/${breed.id}`}>{breed.name}</Link>
                </div>
                )
            })}
          </div>

        </>
    )
}

export default BreedsPage