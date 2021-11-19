import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link, useParams } from 'react-router-dom';
import { allPets, removePet } from '../../store/pets';
import { useHistory } from 'react-router';
import './Breed.css'



const BreedsPage = () => {
    const breeds = useSelector(state => state.breeds)


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