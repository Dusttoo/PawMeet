import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useSelector } from "react-redux";
import { useParams } from "react-router";
import "./Forum.css";
import { addAComment } from "../../store/post_comments";
import SunEditor from "suneditor-react";
import plugins from "suneditor/src/plugins";
import "suneditor/dist/css/suneditor.min.css";

const AddComment = ({ setCommentForm }) => {
  const { postId } = useParams();
  const [validationErrors, setValidationErrors] = useState([]);
  const dispatch = useDispatch();
  const [comment_body, setBody] = useState("");
  const user_id = useSelector((state) => state.session.user.id);
  const currentDate = new Date();
  let month = currentDate.getMonth();
  let day = currentDate.getDate();
  if (currentDate.getMonth() + 1 < 10) {
    month = `0${month + 1}`
  }
  if (currentDate.getDate() < 10) {
    day = `0${day}`
  }
  let posted = `${month}-${day}-${currentDate.getFullYear()}`;
  

  const validate = () => {
    const validationErrors = [];
    if (comment_body.length < 6) {
      validationErrors.push("Comment must be at least 6 characters.");
    }

    return validationErrors;
  };

  const createContent = (content) => {
    setBody(content);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log('posted', posted)
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
      const added = await dispatch(addAComment(createdComment));
      if (added) setCommentForm(false);
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
      <div className="comment-form-container">
        <form className="comment-form" onSubmit={handleSubmit}>
          <div className="comment-form-con">
            <label className="comment-form-label">Message:</label>
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
              <button className="comment-form-button" type="submit">
                Submit
              </button>
            </div>
          </div>
        </form>
      </div>
    </>
  );
};

export default AddComment;
