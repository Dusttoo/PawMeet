import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link, useParams } from 'react-router-dom';
import DisplayPosts from '../Forum/DisplayPost';
import './Profiles.css'


const UserProfile = () => {
    const {id} = useParams();
    const dispatch = useDispatch();
    const users = useSelector(state => state.users)
    const currentUserId = useSelector(state => state.session.user.id)
    const pets = useSelector(state => state.pets)
    const thesePets = []
    const posts = useSelector(state => state.forum)
    const index = 0

    const thesePosts = []
    Object.values(posts).map(post => {
        if (+post.user_id === +id) {
            thesePosts.push(post)
        }
    })

    const sortedByTime = thesePosts.sort(function(a,b){
      return new Date(b.posted) - new Date(a.posted) 
  })


    Object.values(pets).map(pet => {
        if(+pet.owner_id === +id) {
            thesePets.push(pet)
        }
    })


    const modifyTime = () => {
        const date = users[id].barking_since.replace('00:00:00 GMT', '')
        return date

    }

    const getTenPosts = () => {
      return sortedByTime.splice(index, 3)

  }

    return (
        <>
            <div className='user-page'>
                <div className='user-container'>
                    <div className='user-header'>
                        <img className='profile-img' src={users[id].profile_img} alt={users[id].first_name}></img>
                        <div className='user-details-header'>
                            <h1>{users[id].first_name} {users[id].last_name}</h1>
                            <p>Barking since: {modifyTime()}</p>
                        </div>
                    </div>
                    <div className='user-content'>
                        <div className='pet-links'>
                            <h3>Pets:</h3>
                            <div className='pet-links-container'>
                                {thesePets.length === 0 ? 
                                <h2>No pets to display.</h2> : <></>}
                                {thesePets.map(pet => {
                                 return (
                                     <Link className='pet-link' to={`/pets/${pet.id}`}>
                                         <div className='pet-link-details'>
                                            <img className='pet-link-image' src={pet.profile_img} alt={pet.name}/>
                                            <p className='pet-link-name'>{pet.name}</p>
                                         </div>

                                    </Link>
                                 )

                                })}
                            </div>
                        </div>
                        <div className='user-posts'>
                            <h3>Recent Posts:</h3>
                            <div className='user-post-list'>
                                {getTenPosts().map((post) => {
                            return (
                                <DisplayPosts post={post}/>
                            )
                        })}
                            </div>
                        </div>
                    </div>
                    {/* <button className='add-friend'>Add Friend</button> */}
                    {+id === +currentUserId ? 
                    <Link className='add-pet' to='/pets/add'>Add a pet</Link> : <></>}
                </div>
            </div>
        </>
    )
}

export default UserProfile