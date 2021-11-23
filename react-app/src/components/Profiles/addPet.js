import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link, useParams } from 'react-router-dom';
import { addAPet, allPets } from '../../store/pets';
import { useHistory } from 'react-router';

import './Profiles.css'


const AddPet = () => {
const [validationErrors, setValidationErrors] = useState([]);
const dispatch = useDispatch()
const breeds = useSelector(state => state.breeds)
const [profile_img, setProfileImg] = useState('')
const [name, setName] = useState('')
const [breed, setBreed] = useState('')
const [age, setAge] = useState('')
const [description, setDescription] = useState('')
const owner_id = useSelector(state => state.session.user.id)
const history = useHistory();

const validate = () => {
    const validationErrors = [];
    return validationErrors;
}

const handleSubmit = async (e) => {
    e.preventDefault();
        const createdPet = {
          owner_id,
          profile_img,
          name,
          breed,
          age,
          description
        };
        const errors = validate();

        if (errors.length > 0) {
            setValidationErrors(errors);
        } else {
            setValidationErrors([]);
            const added = await dispatch(addAPet(createdPet));
            if(added) {
              history.push(`/users/${owner_id}`)
            }
            
        };

}

    return (
        <>
        {validationErrors.length > 0 && (
        <div className="errors">
            <p className="error-title"> The following errors were found: </p>
            <ul className="error-list">
                {validationErrors.map(error => <li className="error" key={error}>{error}</li>)}
            </ul>
        </div>
        )}
        <div className='add-pet-container'>
            <form className='add-pet-form' onSubmit={handleSubmit}>
                <div className='edit-pet'>
                    <label className='pet-label'>Name:</label>
                    <input
                    placeholder="Pet Name"
                    className='pet-input'
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    required/>
                    <label className='pet-label'>Breed:</label>
                    <select
                    placeholder="Breed"
                    className='pet-input'
                    value={breed}
                    onChange={(e) => setBreed(e.target.value)}
                    required>
                        <option value={breed}>{breed}</option>
                        {Object.values(breeds).map((breed) => {
                            return (
                                <option value={breed.name}>{breed.name}</option>
                            )
                        })}
                    </select>
                    <label className='pet-label'>Age:</label>
                    <input
                    placeholder="Age in years"
                    className='pet-input'
                    value={age}
                    onChange={(e) => setAge(e.target.value)}
                    required/>
                    <label className='pet-label'>Profile Image:</label>
                    <input
                    placeholder="Profile image url"
                    className='pet-input'
                    value={profile_img}
                    onChange={(e) => setProfileImg(e.target.value)}
                    required/>
                    <label className="pet-label" >Description:</label>
                    <textarea
                    placeholder="Post Body"
                    className="pet-description-input"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    required/>
                <button className="pet-button" type="submit">Submit</button>
                </div>
            </form>
        </div>
            
        </>
    )
}

export default AddPet