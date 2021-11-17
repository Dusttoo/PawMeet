import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { allPosts } from '../../store/forum';
import { useSelector } from 'react-redux';
import './Forum.css'
import { Link } from 'react-router-dom';

const DisplayPosts = ({post}) => {
    const authors = useSelector(state => state.users)
    const author = Object.keys(authors).find(thisAuthor => +post.user_id === +thisAuthor)
    const comments = useSelector(state => state.comments)
    const theseComments = []

    Object.keys(comments).map((commentId) => {
        const comment = Object.values(comments).find(thisComment => thisComment.post_id === post.id)
        if(!theseComments.includes(comment)) {
            theseComments.push(comment)
        }
        
    })

    const openPost = () => {

    }


    return (
        <>
            
                <tr onClick={openPost}>  
                    <Link to={`/users/${author}`}><td><img className="profile-icon" src={authors[author].profile_img } alt={authors[author].name}/></td></Link>
                    <Link to={`/forum/posts/${post.id}`}><td>{post.title}</td></Link>
                    <td>{post.posted}</td>
                    <td>{theseComments.length}</td>
                 </tr>  
        </>
    )
}

export default DisplayPosts