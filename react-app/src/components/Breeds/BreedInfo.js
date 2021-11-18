import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link, useParams } from 'react-router-dom';
import { allPets, removePet } from '../../store/pets';
import { useHistory } from 'react-router';
import './Breed.css'



const BreedInfo = () => {
    const {id} = useParams()
    const breeds = useSelector(state => state.breeds)


    return (
        <>
          <div className='breed-container'>
              <h1>{breeds[id].name}</h1>
          </div>

        </>
    )
}

export default BreedInfo