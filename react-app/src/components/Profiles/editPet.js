import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link, useParams } from 'react-router-dom';
import { allPets } from '../../store/pets';
import { editAPet } from '../../store/pets';
import { useHistory } from 'react-router';
import './Profiles.css'


const EditPet = () => {
const {id} = useParams()
const [validationErrors, setValidationErrors] = useState([]);
const dispatch = useDispatch()
const breeds = useSelector(state => state.breeds)
const pets = useSelector(state => state.pets)
const [profile_img, setProfileImg] = useState(pets[id].profile_img)
const [name, setName] = useState(pets[id].name)
const [breed, setBreed] = useState(pets[id].breed)
const [age, setAge] = useState(pets[id].age)
const [description, setDescription] = useState(pets[id].description)
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
            const added = await dispatch(editAPet(createdPet, +id));
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
            <form className='pet-form' onSubmit={handleSubmit}>
                <div className='add-pet'>
                    <label className='form-label'>Name:</label>
                    <input
                    placeholder="Pet Name"
                    className='form-input'
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    required/>
                    <label className='form-label'>Breed:</label>
                    <select
                    placeholder="Breed"
                    className='form-input'
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
                    <label className='form-label'>Age:</label>
                    <input
                    placeholder="Age in years"
                    className='form-input'
                    value={age}
                    onChange={(e) => setAge(e.target.value)}
                    required/>
                    <label className='form-label'>Profile Image:</label>
                    <input
                    placeholder="Profile image url"
                    className='form-input'
                    value={profile_img}
                    onChange={(e) => setProfileImg(e.target.value)}
                    required/>
                    <label className="form-label" >Description:</label>
                    <textarea
                    placeholder="Post Body"
                    className="form-input"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    required/>
                <button className="form-button" type="submit">Submit</button>
                </div>
            </form>
        </div>
            
        </>
    )
}

export default EditPet