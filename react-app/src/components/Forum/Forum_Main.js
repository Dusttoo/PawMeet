import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { allPosts } from '../../store/forum';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import './Forum.css'
import DisplayPosts from './DisplayPost';
import { allUsers } from '../../store/users';
const ForumHome = () => {
    const dispatch = useDispatch()
    const posts = useSelector(state => state.forum)

    useEffect(() => {
      dispatch(allPosts())
      dispatch(allUsers())
  }, [dispatch]);

    return (
        <>
            <h1>Speak!</h1>
            <div className="forum-options">
                <Link to='/forum/add' className='add-post'>Add Post</Link>
            </div>
            <table>
                <tr>
                    <th>Author</th>
                    <th>Title</th>
                    <th>Date</th>
                    <th>Comments</th>
                </tr>
                
                    {Object.values(posts).map((post) => {
                        return (
                            <DisplayPosts post={post}/>
                        )
                    })}
                
            </table>
        </>
    )
}

export default ForumHome