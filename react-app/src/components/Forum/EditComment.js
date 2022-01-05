import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useSelector } from "react-redux";
import { useParams } from "react-router";
import { useHistory } from "react-router";
import "./Forum.css";
import { editAComment } from "../../store/post_comments";
import SunEditor from "suneditor-react";
import plugins from "suneditor/src/plugins";
import "suneditor/dist/css/suneditor.min.css";

const EditComment = ({ commentId, setEditForm }) => {
  const { postId } = useParams();
  const comments = useSelector((state) => state.post_comments);
  const [validationErrors, setValidationErrors] = useState([]);
  const dispatch = useDispatch();
  const [comment_body, setBody] = useState(comments[commentId].comment_body);
  const user_id = useSelector((state) => state.session.user.id);
  const currentDate = new Date();
  let month = currentDate.getMonth();
  let day = currentDate.getDate();
  if (currentDate.getMonth() + 1 < 10) {
    month = `0${month + 1}`;
  }
  if (currentDate.getDate() < 10) {
    day = `0${day}`;
  }
  let posted = `${month}-${day}-${currentDate.getFullYear()}`;
  const history = useHistory();

  const validate = () => {
    const validationErrors = [];
    return validationErrors;
  };

  const createContent = (content) => {
    setBody(content);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const createdComment = {
      user_id,
      post_id: postId,
      comment_body,
      posted,
    };
    const errors = validate();

    if (errors.length > 0) {
      setValidationErrors(errors);
    } else {
      setValidationErrors([]);
      const added = await dispatch(editAComment(createdComment, commentId));
      if (added) {
        history.push(`/forum/posts/${postId}`);
        setEditForm(false);
      }
    }
  };

  return (
    <>
      {validationErrors.length > 0 && (
        <div className="errors">
          <p className="error-title"> The following errors were found: </p>
          <ul className="error-list">
            {validationErrors.map((error) => (
              <li className="error" key={error}>
                {error}
              </li>
            ))}
          </ul>
        </div>
      )}
      <div className="edit-form-container">
        <form className="post-form" onSubmit={handleSubmit}>
          <div className="add-form-con">
            <label className="form-label">Message:</label>
            <div className="editor-container">
              <SunEditor
                height="200px"
                width="100%"
                placeholder="Please type here..."
                onChange={createContent}
                setContents={comment_body}
                setOptions={{
                  plugins: plugins,
                  buttonList: [
                    ["undo", "redo"],
                    ["font", "fontSize", "formatBlock"],
                    // "/", // Line break
                    ["paragraphStyle", "blockquote"],
                    [
                      "bold",
                      "underline",
                      "italic",
                      "strike",
                      "subscript",
                      "superscript",
                    ],
                    ["fontColor", "hiliteColor"],
                    // "/", // Line break
                    [
                      "removeFormat",
                      "outdent",
                      "indent",
                      "align",
                      "horizontalRule",
                      "list",
                    ],
                    ["table", "link", "image", "video"],
                    // "/", // Line break
                    ["fullScreen"],
                    ["preview"],
                  ],
                }}
              />
            </div>
            <div className="submit-container">
              <button className="form-button" type="submit">
                Submit
              </button>
            </div>
          </div>
        </form>
      </div>
    </>
  );
};

export default EditComment;
