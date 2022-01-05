import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { addAPost } from "../../store/forum";
import { useSelector } from "react-redux";
import { useHistory } from "react-router";
import SunEditor from "suneditor-react";
import plugins from "suneditor/src/plugins";
import "suneditor/dist/css/suneditor.min.css";




import "./Forum.css";

const AddPost = () => {
  const [validationErrors, setValidationErrors] = useState([]);
  const dispatch = useDispatch();
  const [title, setTitle] = useState("");
  const [post_body, setBody] = useState("");
  const user_id = useSelector((state) => state.session.user.id);
  const currentDate = new Date();
  const posted = `${
    currentDate.getMonth() + 1
  }-${currentDate.getDate()}-${currentDate.getFullYear()}`;
  const breed_groups = useSelector((state) => state.groups);
  const [group_id, setGroup] = useState(null);
  const history = useHistory();


  const validate = () => {
    const validationErrors = [];
    if (!title) {
      validationErrors.push("Please enter a title");
    }
    if (title.length < 6 || title.length > 30) {
      validationErrors.push("Title must be between 6 and 30 characters");
    }
    if (!post_body) {
      validationErrors.push("Please enter a post body");
    }
    if (post_body.length < 6 || post_body.length > 1000) {
      validationErrors.push("Post body must be between 6 and 1000 characters");
    }

    return validationErrors;
  };

  const createContent = (content) => {
    setBody(content);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
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
      const added = await dispatch(addAPost(createdPost));
      if (added) {
        history.push(`/forum/posts/${added.id}`);
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
              <option value="" disabled selected>
                Please select a group
              </option>
              {Object.values(breed_groups).map((group) => {
                return <option value={group.id}>{group.name}</option>;
              })}
            </select>
            <label className="form-label">Body:</label>
            {/* <textarea
              placeholder="Post Body"
              className="form-input"
              value={post_body}
              onChange={(e) => setBody(e.target.value)}
              required
            /> */}
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
                    ["removeFormat", "outdent", "indent",
                    "align", "horizontalRule", "list"],
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

export default AddPost;
