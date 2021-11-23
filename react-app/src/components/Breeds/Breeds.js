import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link, useParams } from 'react-router-dom';
import { allPets, removePet } from '../../store/pets';
import { useHistory } from 'react-router';
import './Breed.css'
import { allBreedTraits } from '../../store/breed_traits';
import { allBreedAnswers } from '../../store/breed_answers';
import Loading from '../Loading/Loading';




const BreedsPage = () => {
    const breeds = useSelector(state => state.breeds)
    const images = useSelector(state => state.breed_images)
    const dispatch = useDispatch()
    const [loaded, setLoaded] = useState(false);
    const [loading, setLoading] = useState(true);



    useEffect(() => {
    (async() => {
      await dispatch(allBreedTraits())
      await dispatch(allBreedAnswers())
      setLoaded(true);
      setLoading(false);

    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }


    return (
        <>
        {loading ? 
        <>
        <Loading />
        
        </> :
          <div className='breed-list-container'>
            <h2 className='breed-list-heading'>Meet the Breeds</h2>
            {Object.values(breeds).sort(function(a, b) {
              let nameA = a.name.toUpperCase();
              let nameB = b.name.toUpperCase();
              if (nameA < nameB) {
                  return -1;
                }
                if (nameA > nameB) {
                  return 1;
                }
                return 0;
            }).map((breed) => {
              const thisImage = Object.values(images).find((image) => image.breed_id === breed.id)
                return (
                <div className='breed-list-item-container'>
                  <img className='breed-link-image' src={thisImage.img_url} alt={breed.name}/>
                  <Link className='breed' to={`/breeds/${breed.id}`}>{breed.name}</Link>
                </div>
                )
            })}
          </div>}

        </>
    )
}

export default BreedsPage