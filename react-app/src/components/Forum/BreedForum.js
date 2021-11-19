import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { allPosts } from '../../store/forum';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import './Forum.css'
import DisplayPosts from './DisplayPost';
import { allUsers } from '../../store/users';
import { allComments } from '../../store/comments';
import ForumSidebar from './SideBar';
import { useParams } from 'react-router';
const BreedForum = () => {
    const dispatch = useDispatch()
    const {id} = useParams()
    const posts = useSelector(state => state.forum)
    const breed_groups = useSelector(state => state.groups)
    const thesePosts = []
    const headerImage = [
        'https://www.petfoodprocessing.net/ext/resources/PFP-Images/Articles-20/092920_Eukanuba-Premium-Performance_Lead.jpg?t=1601328222&width=1080',
        'https://imagesvc.meredithcorp.io/v3/mm/image?q=85&c=sc&rect=2%2C0%2C2000%2C1332&poi=face&w=2000&h=1333&url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2020%2F10%2F26%2Fbasset-hound-167768274-2000.jpg',
        'https://res.cloudinary.com/jacepharm/image/upload/v1548864318/Depositphotos_64511131_xl-2015-min_efkipp.jpg',
        'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/single-minded-royalty-free-image-997141470-1558380148.jpg?crop=1.00xw:0.755xh;0,0.103xh&resize=640:*',
        'https://www.purina.co.uk/sites/default/files/styles/ttt_image_510/public/2020-11/Toy%20Dogs%20Everything%20You%20Need%20to%20Know2.jpg?itok=lWaCco9f',
        'https://www.nativebreed.org/wp-content/uploads/2020/06/Bulldog.jpg',
        'https://thehappypuppysite.com/wp-content/uploads/2018/01/herding.jpg',



    ]

    useEffect(() => {
      dispatch(allPosts())
      dispatch(allUsers())
      dispatch(allComments())
  }, [dispatch]);

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
                
                    {Object.values(posts).map((post) => {
                        if(+post.group_id === +id) {
                            thesePosts.push(post)
                            return (
                            <DisplayPosts post={post}/>
                        )
                        }
                    })}
                    
            </table>
               {thesePosts.length ? <></> : <h2>No Posts Yet!</h2>}
          </div>
        </div>
        </>
    )
}

export default BreedForum