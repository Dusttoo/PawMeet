import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { addAPost, allPosts } from '../../store/forum';
import { useSelector } from 'react-redux';
import { useParams } from 'react-router';
import { useHistory } from 'react-router';

import './Forum.css'
import { addAComment} from '../../store/post_comments';

const AddComment = ({setCommentForm }) => {
const {postId} = useParams()
const [validationErrors, setValidationErrors] = useState([]);
const dispatch = useDispatch()
const [title, setTitle] = useState('')
const [comment_body, setBody] = useState('')
const user_id = useSelector(state => state.session.user.id)
const currentDate = new Date()
const posted = `${currentDate.getMonth()}-${currentDate.getDate()}-${currentDate.getFullYear()}`
    const history = useHistory();

    const validate = () => {
        const validationErrors = [];

        return validationErrors;
    }

const handleSubmit = async (e) => {
    e.preventDefault();
        const createdComment = {
          user_id,
          post_id: postId,
          comment_body,
          posted
        };
        const errors = validate();

        if (errors.length > 0) {
            setValidationErrors(errors);
        } else {
            setValidationErrors([]);
            const added = await dispatch(addAComment(createdComment));
            if(added) setCommentForm(false)
            
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
        <div className="comment-form-container">
            <form className='comment-form' onSubmit={handleSubmit}>
              <div className="comment-form-con">
                <label className="comment-form-label" >Message:</label>
                        <textarea
                        placeholder="Comment Body"
                        className="comment-form-input"
                        value={comment_body}
                        onChange={(e) => setBody(e.target.value)}
                        required/>
                <div className='submit-container'><button className="comment-form-button" type="submit">Submit</button></div>
              </div>
            </form>
          </div>
        </>
    )
}

export default AddComment