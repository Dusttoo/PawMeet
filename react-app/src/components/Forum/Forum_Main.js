import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { allPosts } from '../../store/forum';
import { useSelector } from 'react-redux';
import './Forum.css'
import DisplayPosts from './DisplayPost';
import { allUsers } from '../../store/users';
const ForumHome = () => {
    const dispatch = useDispatch()
    const posts = useSelector(state => state.forum)
    const users = useSelector(state => state.session.users)

    useEffect(() => {
      dispatch(allPosts())
      dispatch(allUsers())
  }, [dispatch]);

    return (
        <>
            <h1>Forum</h1>
            <table>
                <tr>
                    <th>Author</th>
                    <th>Title</th>
                    <th>Date</th>
                    <th>Comments</th>
                </tr>
                
                    {Object.values(posts).map((post) => {
                        return (
                            <DisplayPosts post={post} users={users}/>
                        )
                    })}
                
            </table>
        </>
    )
}

export default ForumHome