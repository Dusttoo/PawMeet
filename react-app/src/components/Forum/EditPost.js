import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { allPosts } from '../../store/forum';
import { useSelector } from 'react-redux';
import { useParams } from 'react-router';
import { useHistory } from 'react-router';
import { editAPost } from '../../store/forum';

import './Forum.css'

const EditPost = ({setEditForm}) => {
const {postId} = useParams()
const posts = useSelector(state => state.forum)

const [validationErrors, setValidationErrors] = useState([]);
const dispatch = useDispatch()
const [title, setTitle] = useState(posts[postId].title)
const [post_body, setBody] = useState(posts[postId].post_body)
const user_id = useSelector(state => state.session.user.id)
const posted = posts[postId].posted

    const history = useHistory();

    const validate = () => {
        const validationErrors = [];

        return validationErrors;
    }

const handleSubmit = async (e) => {
    e.preventDefault();
        const createdPost = {
          user_id,
          title,
          post_body,
          posted
        };
        console.log(createdPost, 'created post')
        const errors = validate();

        if (errors.length > 0) {
            setValidationErrors(errors);
        } else {
            console.log('before dispatch')
            setValidationErrors([]);
            const added = await dispatch(editAPost(createdPost));
            console.log('added', added)
            if(added) {
              history.push(`/posts/${added.id}`)
            }
            
        };

}


    return (
        <>
            {validationErrors.length > 0 && (
        <div className="errors">
            <p className="error-title"> The following errors were found: </p>
            <ul className="error-list">
                {validationErrors.map(error => <li className="error" key={error}>{error}</li>)}
            </ul>
        </div>
        )}
        <div className="add-form-container">
            <form className='post-form' onSubmit={handleSubmit}>
              <div className="add-form-con">
                <label className="form-label" >Title:</label>
                        <input
                        placeholder="Title"
                        className="form-input"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        required/>
                <label className="form-label" >Body:</label>
                        <textarea
                        placeholder="Post Body"
                        className="form-input"
                        value={post_body}
                        onChange={(e) => setBody(e.target.value)}
                        required/>
                <button className="form-button" type="submit">Submit</button>
              </div>
            </form>
          </div>
        </>
    )
}

export default EditPost