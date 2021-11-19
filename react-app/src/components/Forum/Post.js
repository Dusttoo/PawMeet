import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { allPosts, removePost } from '../../store/forum';
import { useSelector } from 'react-redux';
import { useParams, useHistory} from 'react-router';
import EditPost from './EditPost';
import AddComment from './AddComment';
import './Forum.css'
import DisplayComments from './DisplayComment';
import { postComments } from '../../store/post_comments';
import { Link } from 'react-router-dom';
import { addALike, removeLike } from '../../store/likes';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHeart, faPenSquare} from '@fortawesome/free-solid-svg-icons'
import { faStopCircle, faMinusCircle } from '@fortawesome/free-solid-svg-icons';


const Posts = () => {
    const { postId } = useParams();
    const [loaded, setLoaded] = useState(false);
    const history = useHistory()
    const dispatch = useDispatch()
    const currentUser = useSelector(state => state.session.user)
    const posts = useSelector(state => state.forum)
    const users = useSelector(state => state.users)
    const likes = useSelector(state => state.likes)
    const comments = useSelector(state => state.post_comments)
    const author = Object.keys(users).find((user) => (+user === +posts[postId].user_id))
    const thisUser = useSelector(state => state.session.user)
    const [editForm, setEditForm] = useState(false)
    const [commentForm, setCommentForm] = useState(false)
    const liked = Object.values(likes).map((like) => {
        if(+like.post_id === +postId) {
        if(+like.user_id === +currentUser.id) {
            return true
        } 
        return false
        }
        
    })

     useEffect(() => {
    (async() => {
      await dispatch(allPosts())
      await dispatch(postComments(postId))
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

    const getLikes = () => {
        let numLikes = 0;
        Object.values(likes).map((like) => {
            if(+like.post_id === +postId) {
                numLikes++
            }
        })
        return numLikes

    }
    console.log(getLikes())



    const openEditForm = () => {
        if(editForm) {
            setEditForm(false)
        } else {
            setEditForm(true)
        }
    }

    const deletePost = () => {
        dispatch(removePost(postId));
            history.push(`/forum`)
    }

    const openCommentForm = () => {
        if (commentForm) {
            setCommentForm(false)
        } else {
            setCommentForm(true)
        }
    }

    const addLike = () => {
        const createdLike = {
          user_id: currentUser.id,
          post_id: postId,
        };
        dispatch(addALike(createdLike))
    }

    const deleteLike = () => {
        const likeId = Object.values(likes).find((like) => +like.user_id === +currentUser.id)
        dispatch(removeLike(+likeId.id))
    }

    return (
        <>
            <div className="post-container">
                <div className='post'>
                    {thisUser.id === +author ?
                    <div className='post-user-options'>
                        <FontAwesomeIcon className='edit-button' onClick={openEditForm} icon={faPenSquare}/>
                        <FontAwesomeIcon className='delete-button' onClick={deletePost} icon={faMinusCircle }/>
                    </div> : <></>}
                    {editForm ?
                    <EditPost setEditForm={setEditForm}/> : <></>}
                    <div className="post-header">
                        <div className="author-details">
                            <Link to={`/users/${author}`} ><img className='profile-icon' src={users[author].profile_img} alt={users[author].first_name}/></Link>
                            <p>{users[author].first_name} {users[author].last_name}</p>
                        </div>
                        <div className='post-title-container'>
                            <h1 className="show-post-title">{posts[postId].title}</h1>
                        </div>
                    </div>
                    <div className='post-body-container'>
                        <p>{posts[postId].post_body}</p>
                    </div>
                    
                        {!liked.includes(true) ? 
                        <div className='likes-container'>
                            <FontAwesomeIcon className='like-heart' onClick={addLike} icon={faHeart} style={{color: '#d3d3d3'}}/> 
                            {getLikes()}
                        </div> 
                        : 
                        <div className='likes-container'>
                            <FontAwesomeIcon className='like-heart' onClick={deleteLike} icon={faHeart} style={{color: '#ff0808'}}/>
                            {getLikes()}
                        </div> }

                        
                </div>
            </div>
            <div className="comment-container">
                <div className='post'>

                    <div className='comment-options-container'>
                        <button 
                    onClick={openCommentForm}>Add a comment</button>
                    </div>
                    {commentForm ? 
                    <AddComment setCommentForm={setCommentForm}/> : <></>}
                    <table className='comments-table'>
                    {Object.values(comments).map((comment) => {
                        return <DisplayComments commentId={comment.id}/>
                    })}


                    </table>
                </div>
            </div>
        </>
    )
}

export default Posts