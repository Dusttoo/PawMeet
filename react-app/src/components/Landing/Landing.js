import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import ReactPlayer from 'react-player'
import './Landing.css'


const Landing = () => {
const breeds = useSelector(state => state.breeds)
const breedImages = useSelector(state => state.breed_images)
const breedGroups = useSelector(state => state.groups)
const posts = useSelector(state => state.forum)
const index = 0

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min); //The maximum is exclusive and the minimum is inclusive
}
  const getTenPosts = () => {
      return sortedByTime.splice(index, 10)

  }
    const users = useSelector(state => state.users)
const highlightedBreed = breeds[getRandomInt(0, Object.keys(breeds).length)]
const highlightedImage = Object.values(breedImages).find(image => image.breed_id === highlightedBreed.id)
const highlightedGroup = Object.values(breedGroups).find(group => +group.id === +highlightedBreed.breed_group)
const sortedByTime = Object.values(posts).sort(function(a,b){
      return new Date(b.posted) - new Date(a.posted) 
  })

    return (
        <>
            <div className='landing-container'>
                <div className='landing-header'>
                    <h1 className='intro'>Welcome to Paw Meet!</h1>
                    <h2 className='tagline'>A place to discover man's next best friend</h2>
                </div>
                <div className='highlighted-breed-container'>
                    <ReactPlayer 
                    url={highlightedBreed.breed_video} 
                    muted={true}
                    playing={true}/>
                    <div className='highlighted-breed-details'>
                        <Link to={`/breeds/${highlightedBreed.id}`} className='highlighted-breed-name'>{highlightedBreed.name}</Link>
                        <h3 className='highlighted-breed-group'>{highlightedGroup.name}</h3>
                    </div>
                </div>
                <div className='recent-posts-container'>
                    <h3 className='recent-posts-header'>What's everyone barking about?</h3>
                    <table className='recent-posts'>
                    {getTenPosts().map((post) => {
                    const author = Object.keys(users).find((user) => (+user === +post.user_id))

                    return (
                        <tr>
                            <td>
                                <div className='comment-info'>
                                    <Link to={`/users/${author}`} ><img className='profile-icon' src={users[author].profile_img} alt={users[author].first_name}/></Link>
                                    <div className='name-date'>
                                        <Link className='author-name' to={`/users/${author}`}>{users[author].first_name} {users[author].last_name}</Link>
                                    </div>
                                </div>
                            </td>
                            <td><Link to={`/forum/posts/${post.id}`}>{post.title}</Link></td>

                        </tr>
                        
                        )                        
                    })}
                    </table>
                </div>
            </div>
        </>
    )
}

export default Landing