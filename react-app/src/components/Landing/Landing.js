import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import ReactPlayer from 'react-player'
import { allUsers } from '../../store/users';
import { allPosts } from '../../store/forum';
import { allPets } from '../../store/pets';
import { allBreeds } from '../../store/breeds';
import { allGroups } from '../../store/breed_groups';
import { allImages } from '../../store/breed_images';
import DisplayPosts from '../Forum/DisplayPost';
import './Landing.css'
import { allComments } from '../../store/comments';
import BreedsPage from '../Breeds/Breeds';
import GifPlayer from 'react-gif-player'
import Loading from '../Loading/Loading';


const Landing = () => {
const dispatch = useDispatch()
const breeds = useSelector(state => state.breeds)
function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min); //The maximum is exclusive and the minimum is inclusive
}
const randnum = getRandomInt(1, Object.keys(breeds).length - 1)
const highlightedBreed = breeds[randnum]
const breedImages = useSelector(state => state.breed_images)
const breedGroups = useSelector(state => state.groups)
const posts = useSelector(state => state.forum)
const index = 0
const [loading, setLoading] = useState(true);
const users = useSelector(state => state.users)
const highlightedImage = Object.values(breedImages).find(image => image.breed_id === highlightedBreed.id)
const highlightedGroup = Object.values(breedGroups).find(group => +group.id === +highlightedBreed.breed_group)
const sortedByTime = Object.values(posts).sort(function(a,b){
      return new Date(b.posted) - new Date(a.posted) 
  })


  useEffect(() => {
    (async() => {
      await dispatch(allUsers())
      await dispatch(allPosts())
      await dispatch(allPets())
      await dispatch(allBreeds())
      await dispatch(allGroups())
      await dispatch(allImages())
      await dispatch(allComments())
      setLoading(false);
    })();
  }, [dispatch]);


  const getTenPosts = () => {
      return sortedByTime.splice(index, 5)

  }


    return (
        <>
        {loading ? 
        <>
        <Loading />
        
        </> :
        <>
            <div className='landing-container'>
                <div className='landing-header'>
                     
                    <h1 className='intro'>Welcome to Paw Meet!</h1>
                    <h2 className='tagline'>A place to discover man's next best friend</h2>
                    <Link to='/breed-quiz' className='tagline-breed-quiz'>Take our quiz to find the perfect breed for you!</Link>

                </div>
                <div className='highlighted-breed-container'>
                    <ReactPlayer 
                    width={'50%'}
                    url={highlightedBreed.breed_video} 
                    muted={true}
                    playing={true}/>
                    <div className='highlighted-breed-details'>
                        <Link to={`/breeds/${highlightedBreed.id}`} className='highlighted-breed-name'>{highlightedBreed.name}</Link>
                        <h3 className='highlighted-breed-group'>{highlightedGroup.name} Group</h3>
                    </div>
                </div>
                <div className='bottom-content'>
                    <div className='recent-posts-container'>
                        <h2 className='breed-list-heading'>What's everyone barking about?</h2>
                        <table className='recent-posts'>
                    <tr>
                        <th style={{width:'10%'}} className="table-label">Author</th>
                        <th style={{width:'65%'}} className="table-label">Title</th>
                        <th style={{width:'23%'}} className="table-label">Date</th>
                        <th style={{width:'2%'}} className="table-label">Comments</th>
                    </tr>
                       {getTenPosts().map((post) => {
                            return (
                                <DisplayPosts post={post}/>
                            )
                        })}
                        </table>
                    </div>
                    <div className='breed-highlights-container'>
                        <BreedsPage />

                    </div>
                </div>
            </div>
        </>}
        </>
    )
}

export default Landing