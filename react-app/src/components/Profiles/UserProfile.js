import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link, useParams } from 'react-router-dom';
import './Profiles.css'


const UserProfile = () => {
    const {id} = useParams();
    const dispatch = useDispatch();
    const users = useSelector(state => state.users)
    const currentUserId = useSelector(state => state.session.user.id)
    const pets = useSelector(state => state.pets)
    const thesePets = []

    Object.values(pets).map(pet => {
        if(+pet.owner_id === +id) {
            thesePets.push(pet)
        }
    })


    const modifyTime = () => {
        const date = users[id].barking_since.replace('00:00:00 GMT', '')
        return date

    }

    return (
        <>
            <div className='user-page'>
                <div className='user-container'>
                    <div className='user-header'>
                        <img className='profile-img' src={users[id].profile_img} alt={users[id].first_name}></img>
                        <div className='user-details-header'>
                            <h1>{users[id].first_name} {users[id].last_name}</h1>
                            <p>Member since: {modifyTime()}</p>
                        </div>
                    </div>
                    <div className='user-content'>
                        <div className='pet-links'>
                            <h3>Pets:</h3>
                            <div className='pet-links-container'>
                                {thesePets.map(pet => {
                                 return (
                                     <Link className='pet-link' to={`/pets/${pet.id}`}>{pet.name}</Link>
                                 )

                                })}
                            </div>
                        </div>
                        <div className='user-posts'>
                            <h3>Recent Posts</h3>
                            <div className='user-post-list'>
                                <p>Post goes here</p>
                            </div>
                        </div>
                    </div>
                    <button className='add-friend'>Add Friend</button>
                    {+id === +currentUserId ? 
                    <Link to='/pets/add'>Add a pet</Link> : <></>}
                </div>
            </div>
        </>
    )
}

export default UserProfile