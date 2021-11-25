import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link, useParams } from 'react-router-dom';
import { allPets, removePet } from '../../store/pets';
import EditPet from './editPet';
import AddPet from './addPet';
import { useHistory } from 'react-router';
import './Profiles.css'



const PetProfile = () => {
    const dispatch = useDispatch()
    const history = useHistory()
    const {id} = useParams()
    const pets = useSelector(state => state.pets)
    const [editForm, setEditForm] = useState(false)
    const owner = pets[id].owner_id
    const currentUser = useSelector(state => state.session.user)
    const users = useSelector(state => state.users)

    const openEditForm = () => {
        if (editForm) {
            setEditForm(false)
        } else {
            setEditForm(true)
        }

    }

    const deletePet = () => {
        dispatch(removePet(id));
            history.push(`/users/${owner}`)
    }

    console.log(users[pets[id].owner_id])


    return (
        <>
            <div className='user-page'>
                <div className='user-container'>
                    <div className='user-header'>
                        <img className='profile-img' src={pets[id].profile_img} alt={pets[id].first_name}></img>
                        <div className='pet-details-header'>
                            <h1>{pets[id].name}</h1>
                            <h3>{pets[id].breed}</h3>
                            <h3>{pets[id].age}</h3>
                        </div>
                    </div>
                    <div className='pet-content'>
                        <p>{pets[id].description}</p>
                        <Link className='owner-link' to={`/users/${users[pets[id].owner_id].id}`}>
                            <div className='pet-link-details'>
                                <img className='pet-link-image' src={users[pets[id].owner_id].profile_img} alt={users[pets[id].owner_id].name}/>
                                <p className='pet-link-name'>Owner: {users[pets[id].owner_id].first_name} {users[pets[id].owner_id].last_name}</p>
                            </div>
                        </Link>
                            
                    </div>
                    {owner === currentUser.id ? 
                    <div className='pet-options'>
                        <button 
                        className='pet-button'
                        onClick={openEditForm}>Edit Pet</button>
                        <button
                        className='pet-button'
                        onClick={deletePet}>Delete Pet</button>
                    </div>
                    : <></>}
                    {editForm ?
                    <div className='edit-pet'>
                        <EditPet />
                    </div> : <></>} 
                    
                </div>
                
            </div>
        </>
    )
}

export default PetProfile