import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { allPosts } from '../../store/forum';
import { useSelector } from 'react-redux';
import './Forum.css'
import { Link } from 'react-router-dom';
import { useParams, useHistory } from 'react-router';
import { removeComment } from '../../store/comments';
import EditComment from './EditComment';


const DisplayComments = () => {
    const {postId} = useParams()
    const history = useHistory()
    const dispatch = useDispatch()
    const authors = useSelector(state => state.users)
    const comments = useSelector(state => state.comments)
    const currentUser = useSelector(state => state.session.user)
    const [editForm, setEditForm] = useState(false)
    let author = {}
    const thisComment = Object.values(comments).find(comment => +comment.post_id === +postId)
    if(thisComment) {
        author = Object.keys(authors).find(thisAuthor => +thisComment.user_id === +thisAuthor)
    }
    
    const deleteComment = () => {
        console.log(thisComment.id)
        dispatch(removeComment(thisComment.id));
        // history.push(`/forum/posts/${postId}`)
    }
    
    const openEditForm = () => {

        if(editForm) {
            setEditForm(false)
        } else {
            setEditForm(true)
        }
    }


    return (
        <>
            {!thisComment ? <h2>No comments to display</h2>:
               <tr>  
                    <Link to={`/users/${author}`}><td><img className="profile-icon" src={authors[author].profile_img } alt={authors[author].name}/></td></Link>
                    <td>{thisComment.posted}</td>
                    <td>{thisComment.comment_body}</td>
                    {editForm ? 
                    <EditComment commentId={thisComment.id}/> : <></>}
                    {+authors[author].id === +currentUser.id ?
                    <td>
                        <button className='edit-post'
                        onClick={openEditForm}>Edit</button>
                        <button 
                        className='delete-post'
                        onClick={deleteComment}>Delete</button>
                    </td> : <></>}
                 </tr>  }
        </>
    )
}

export default DisplayComments