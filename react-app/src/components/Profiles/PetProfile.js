import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link, useParams } from 'react-router-dom';
import { allPets } from '../../store/pets';
import EditPet from './editPet';
import AddPet from './addPet';
import './Profiles.css'


const PetProfile = () => {
    const {id} = useParams()
    const pets = useSelector(state => state.pets)
    const [editForm, setEditForm] = useState(false)

    const openEditForm = () => {
        if (editForm) {
            setEditForm(false)
        } else {
            setEditForm(true)
        }

    }

    const deletePet = () => {

    }


    return (
        <>
            <div className='pet-page'>
                <div className='pet-container'>
                    <div className='pet-header'>
                        <img className='pet-profile-img' src={pets[id].profile_img} alt={pets[id].first_name}></img>
                        <div className='pet-details-header'>
                            <h1>{pets[id].name}</h1>
                            <h3>{pets[id].breed}</h3>
                            <h3>{pets[id].age}</h3>
                        </div>
                    </div>
                    <div className='pet-content'>
                        <p>{pets[id].description}</p>

                    </div>
                </div>
                <div className='pet-options'>
                    <button 
                    onClick={openEditForm}>Edit Pet</button>
                    <button
                    onClick={deletePet}>Delete Pet</button>
                </div>
                {editForm ?
                <div className='edit-pet'>
                    <EditPet />
                </div> : <></>}
            </div>
        </>
    )
}

export default PetProfile