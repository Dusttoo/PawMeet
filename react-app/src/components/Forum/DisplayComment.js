import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { allPosts } from '../../store/forum';
import { useSelector } from 'react-redux';
import './Forum.css'
import { Link } from 'react-router-dom';
import { useParams, useHistory } from 'react-router';
import { removeComment } from '../../store/post_comments';
import EditComment from './EditComment';
import { postComments } from '../../store/post_comments';


const DisplayComments = ({commentId}) => {
    const {postId} = useParams()
    const history = useHistory()
    const dispatch = useDispatch()
    const authors = useSelector(state => state.users)
    const theseComments = useSelector(state => state.post_comments)
    const currentUser = useSelector(state => state.session.user)
    const [editForm, setEditForm] = useState(false)
    const [loaded, setLoaded] = useState(false);
    const comment = Object.keys(theseComments).find(comment => +comment === commentId)

    

    let author = 0
    // const thisComment = Object.keys(comments).find(comment => +comment === +commentId)
    


   useEffect(() => {
    (async() => {
     await dispatch(postComments(postId))

      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  if(comment) {
        author = Object.keys(authors).find(thisAuthor => +theseComments[comment].user_id === +thisAuthor)
    } else {
        return null
    }

    

    
    const deleteComment = () => {
        dispatch(removeComment(theseComments[comment].id));
        // history.push(`/forum/posts/${postId}`)
    }
    
    const openEditForm = () => {

        if(editForm) {
            setEditForm(false)
        } else {
            setEditForm(true)
        }
    }

    const modifyTime = () => {
        const date = theseComments[comment].posted.replace('00:00:00 GMT', '')
        return date

    }

    return (
        <>
            {!Object.keys(theseComments) ? <h2>No comments to display</h2>:
                <tr className='comment-row'>  
                  
                    <td className='table-cell' style={{width:'10%'}}>
                        <div className='comment-info'>
                            <Link to={`/users/${author}`}><img className="profile-icon" src={authors[author].profile_img } alt={authors[author].name}/></Link>
                            {modifyTime()}
                        </div>
                    </td>
                    <td className='table-cell' style={{width:'65%'}} className='comment-body'>{theseComments[comment].comment_body}</td>
                    {editForm ? 
                    <EditComment commentId={theseComments[comment].id}/> : <></>}
                    {+authors[author].id === +currentUser.id ?
                    <td className='comment-edit-delete'>
                        <button className='edit-post'
                        onClick={openEditForm}>Edit</button>
                        <button 
                        className='delete-post'
                        onClick={deleteComment}>Delete</button>
                    </td> : <></>}
                 </tr>}
        </>
    )
}

export default DisplayComments