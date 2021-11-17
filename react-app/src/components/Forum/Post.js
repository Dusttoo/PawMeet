import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { allPosts, removePost } from '../../store/forum';
import { useSelector } from 'react-redux';
import { useParams, useHistory } from 'react-router';
import EditPost from './EditPost';
import AddComment from './AddComment';

import './Forum.css'
import DisplayComments from './DisplayComment';

const Posts = () => {
    const { postId } = useParams();
    const [loaded, setLoaded] = useState(false);
    const history = useHistory()
    const dispatch = useDispatch()
    const posts = useSelector(state => state.forum)
    const users = useSelector(state => state.users)
    const comments = useSelector(state => state.comments)
    const author = Object.keys(users).find((user) => (+user === +posts[postId].user_id))
    const thisUser = useSelector(state => state.session.user)
    const [editForm, setEditForm] = useState(false)
    const [commentForm, setCommentForm] = useState(false)

     useEffect(() => {
    (async() => {
      await dispatch(allPosts())
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

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

    return (
        <>
            <div className="post-container">
                {thisUser.id === +author ?
                <div className='post-user-options'>
                    <button className='edit-post'
                    onClick={openEditForm}>Edit</button>
                    <button className='delete-post'
                    onClick={deletePost}>Delete</button>
                </div> : <></>}
                {editForm ?
                <EditPost openEditForm={setEditForm}/> : <></>}
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
            <div className="comment-container">
                <button onClick={openCommentForm}>Add a comment</button>
                {commentForm ? 
                <AddComment /> : <></>}
                <table>
                    <DisplayComments />
                    
                </table>
            </div>
        </>
    )
}

export default Posts