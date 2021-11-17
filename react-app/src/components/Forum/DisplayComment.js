import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { allPosts } from '../../store/forum';
import { useSelector } from 'react-redux';
import './Forum.css'
import { Link } from 'react-router-dom';
import { useParams, useHistory } from 'react-router';
import { removeComment } from '../../store/comments';
const DisplayComments = () => {
    const {postId} = useParams()
    const history = useHistory()
    const dispatch = useDispatch()
    const authors = useSelector(state => state.users)
    const comments = useSelector(state => state.comments)
    const currentUser = useSelector(state => state.session.user)
    let author = {}
    const thisComment = Object.values(comments).find(comment => +comment.post_id === +postId)
    if(thisComment) {
        author = Object.keys(authors).find(thisAuthor => +thisComment.user_id === +thisAuthor)
    }
    
    const deleteComment = () => {
        dispatch(removeComment(postId));
        history.push(`/forum/posts/${postId}`)
    }
    



    return (
        <>
            {!thisComment ? <h2>No comments to display</h2>:
               <tr>  
                    <Link to={`/users/${author}`}><td><img className="profile-icon" src={authors[author].profile_img } alt={authors[author].name}/></td></Link>
                    <td>{thisComment.posted}</td>
                    <td>{thisComment.comment_body}</td>
                    {+authors[author].id === +currentUser.id ?
                    <td>
                        <button className='edit-post'>Edit</button>
                        <button 
                        className='delete-post'
                        onClick={deleteComment}>Delete</button>
                    </td> : <></>}
                 </tr>  }
        </>
    )
}

export default DisplayComments