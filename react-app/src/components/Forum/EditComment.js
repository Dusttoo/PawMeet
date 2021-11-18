import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { addAPost, allPosts } from '../../store/forum';
import { useSelector } from 'react-redux';
import { useParams } from 'react-router';
import { useHistory } from 'react-router';

import './Forum.css'
import { editAComment } from '../../store/comments';

const EditComment = ({commentId}) => {
const {postId} = useParams()
const comments = useSelector(state => state.comments)
const [validationErrors, setValidationErrors] = useState([]);
const dispatch = useDispatch()
const [comment_body, setBody] = useState(comments[commentId].comment_body)
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
            const added = await dispatch(editAComment(createdComment, commentId));
            if(added) {
              history.push(`forum/posts/${postId}`)
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
                <label className="form-label" >Message:</label>
                        <textarea
                        placeholder="Post Body"
                        className="form-input"
                        value={comment_body}
                        onChange={(e) => setBody(e.target.value)}
                        required/>
                <button className="form-button" type="submit">Submit</button>
              </div>
            </form>
          </div>
        </>
    )
}

export default EditComment