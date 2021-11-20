import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { allPostsForGroup } from '../../store/group_posts';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import './Forum.css'
import DisplayPosts from './DisplayPost';
import { allUsers } from '../../store/users';
import { allComments } from '../../store/comments';
import ForumSidebar from './SideBar';
import { useParams } from 'react-router';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAngleLeft, faAngleRight } from '@fortawesome/free-solid-svg-icons';
const BreedForum = () => {
    const dispatch = useDispatch()
    const {id} = useParams()
    const posts = useSelector(state => state.group_posts)
    const breed_groups = useSelector(state => state.groups)
    const thesePosts = []
    const [index, setIndex] = useState(0)
    const remove = 10;
    const headerImage = [
        'https://www.petfoodprocessing.net/ext/resources/PFP-Images/Articles-20/092920_Eukanuba-Premium-Performance_Lead.jpg?t=1601328222&width=1080',
        'https://imagesvc.meredithcorp.io/v3/mm/image?q=85&c=sc&rect=2%2C0%2C2000%2C1332&poi=face&w=2000&h=1333&url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2020%2F10%2F26%2Fbasset-hound-167768274-2000.jpg',
        'https://res.cloudinary.com/jacepharm/image/upload/v1548864318/Depositphotos_64511131_xl-2015-min_efkipp.jpg',
        'https://www.scruffylittleterrier.com/wp-content/uploads/2020/07/AdobeStock_336595006-2880x1800.jpeg',
        'https://blogstudio.s3.amazonaws.com/sitstay/3963c6cbd12033c4a966c0c9a62c9c05.jpg',
        'https://www.nativebreed.org/wp-content/uploads/2020/06/Bulldog.jpg',
        'https://thehappypuppysite.com/wp-content/uploads/2018/01/herding.jpg',



    ]

    useEffect(() => {
      dispatch(allPostsForGroup(id))
      dispatch(allUsers())
      dispatch(allComments())
  }, [dispatch, id]);

    const sortedByTime = Object.values(posts).sort(function(a,b){
      return new Date(b.posted) - new Date(a.posted) 
  })

  const getTenPosts = () => {
      return sortedByTime.splice(index, remove)

  }
  console.log('just the index', index)
  console.log('just the length', sortedByTime.length)


  const showPrevious = () => {
      console.log('previous')
      if(index > 10) {
          console.log('previous index', index)
          setIndex(index - 10)
      }

  }

  const showNext = () => {
      console.log('next', index)
      if(index + 10 <= sortedByTime.length) {
        console.log('next length', sortedByTime.length)

          if( (sortedByTime.length - index) < 10) {
            console.log('next length', sortedByTime.length - index)
                
              setIndex(index + (sortedByTime.length - index))
          } else {
              setIndex(index + 10)
          }
      }

  }

    return (
        <>
        <div className='page-container'>
          <ForumSidebar />
          <div className="forum-container">
            <div className='forum-header-image' style={{backgroundImage: `url(${headerImage[id - 1]})`}}>
                <h1 className="forum-header" >{breed_groups[id].name}</h1>
                </div>
            <div className="forum-options">
                <Link to='/forum/add' className='add-post'>Add Post</Link>
            </div>
            <table className="forum-table">
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
               {Object.keys(posts).length ? <></> : <h2>No Posts Yet!</h2>}
               <div className='next-prev-container'>
                   <FontAwesomeIcon icon={faAngleLeft} 
                   onClick={showPrevious}/>
                   <FontAwesomeIcon icon={faAngleRight} 
                   onClick={showNext}/>
               </div>
          </div>
        </div>
        </>
    )
}

export default BreedForum