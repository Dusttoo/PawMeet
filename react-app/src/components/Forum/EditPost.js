import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useSelector } from "react-redux";
import { useParams } from "react-router";
import { editAPost } from "../../store/forum";
import SunEditor from "suneditor-react";
import plugins from "suneditor/src/plugins";
import "suneditor/dist/css/suneditor.min.css";
import "./Forum.css";

const EditPost = ({ setEditForm }) => {
  const { postId } = useParams();
  const posts = useSelector((state) => state.forum);
  const [validationErrors, setValidationErrors] = useState([]);
  const dispatch = useDispatch();
  const [title, setTitle] = useState(posts[postId].title);
  const [post_body, setBody] = useState(posts[postId].post_body);
  const user_id = useSelector((state) => state.session.user.id);
  const posted = posts[postId].posted;
  const breed_groups = useSelector((state) => state.groups);
  const [group_id, setGroup] = useState(posts[postId].group_id);
  const validate = () => {
    const validationErrors = [];

    return validationErrors;
  };

  const createContent = (content) => {
    setBody(content);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (group_id === 0) {
      setGroup(null);
    }
    const createdPost = {
      user_id,
      title,
      post_body,
      posted,
      group_id,
    };
    const errors = validate();

    if (errors.length > 0) {
      setValidationErrors(errors);
    } else {
      setValidationErrors([]);
      const added = await dispatch(editAPost(createdPost, postId));
      if (added) {
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
      <div className="add-form-container">
        <form className="post-form" onSubmit={handleSubmit}>
          <div className="add-form-con">
            <label className="form-label">Title:</label>
            <input
              placeholder="Title"
              className="small-form-input"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              required
            />
            <label className="form-label">Breed Group:</label>
            <select
              placeholder="Breed"
              className="small-form-select"
              value={group_id}
              onChange={(e) => setGroup(e.target.value)}
              required
            >
              <option value="" disabled>
                Please select a group
              </option>
              <option value={0}>Main</option>
              {Object.values(breed_groups).map((group) => {
                return <option value={group.id}>{group.name}</option>;
              })}
            </select>
            <label className="form-label">Body:</label>
            <div className="editor-container">
              <SunEditor
                height="200px"
                width="100%"
                placeholder="Please type here..."
                onChange={createContent}
                setContents={post_body}
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

export default EditPost;
