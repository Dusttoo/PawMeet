import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { allPosts } from '../../store/forum';
import { useSelector } from 'react-redux';
import { useParams } from 'react-router';

import './Forum.css'

const Posts = () => {
    const { postId } = useParams();
    const posts = useSelector(state => state.forum)
    const users = useSelector(state => state.users)
    const author = Object.keys(users).find((user) => (+user === +posts[postId].id))



    return (
        <>
            <div className="post-container">
                <div className="post-header">
                    <div className="author-details">
                        <img className='profile-icon' src={users[author].profile_img} alt={users[author].first_name}/>
                        <p>{users[author].first_name} {users[author].last_name}</p>
                    </div>
                    <h1 className="post-title">{posts[postId].title}</h1>
                </div>
                <div>
                    <p>{posts[postId].post_body}</p>
                </div>
            </div>
        </>
    )
}

export default Posts