import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link, useParams } from 'react-router-dom';
import { allPets, removePet } from '../../store/pets';
import { useHistory } from 'react-router';
import './Breed.css'
import { allBreedTraits } from '../../store/breed_traits';



const BreedsPage = () => {
    const breeds = useSelector(state => state.breeds)
    const dispatch = useDispatch()
    const [loaded, setLoaded] = useState(false);


    useEffect(() => {
    (async() => {
      dispatch(allBreedTraits())
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
                return (
                <Link to={`/breeds/${breed.id}`}>{breed.name}</Link>
                )
            })}
          </div>

        </>
    )
}

export default BreedsPage