import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useSelector } from "react-redux";
import { addAPet } from "../../store/pets";
import { useHistory } from "react-router";
import validator from "validator";
import ImageUploading from "react-images-uploading";

import "./Profiles.css";

const AddPet = () => {
  const [validationErrors, setValidationErrors] = useState([]);
  const dispatch = useDispatch();
  const breeds = useSelector((state) => state.breeds);
  const [profile_img, setProfileImg] = useState("");
  const [name, setName] = useState("");
  const [breed, setBreed] = useState("");
  const [age, setAge] = useState("");
  const [description, setDescription] = useState("");
  const owner_id = useSelector((state) => state.session.user.id);
  const history = useHistory();
  const letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
  ];
  const [image, setImage] = useState([]);

  const validate = () => {
    const validationErrors = [];
    if (!name) validationErrors.push("Name is required");
    if (name.length < 3)
      validationErrors.push("Name must be at least 3 characters");
    if (!breed) validationErrors.push("Please select a breed");
    if (validator.isIn(age, letters))
      validationErrors.push("Age must only be numbers");
    if (!description) validationErrors.push("Please enter a description");
    if (description.length < 10)
      validationErrors.push("Description must be at least 10 characters");

    return validationErrors;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const createdPet = {
      owner_id,
      profile_img,
      name,
      breed,
      age,
      description,
    };
    const errors = validate();

    if (errors.length > 0) {
      setValidationErrors(errors);
    } else {
      setValidationErrors([]);
      const added = await dispatch(addAPet(createdPet));
      if (added) {
        history.push(`/users/${owner_id}`);
      }
    }
  };

  const onChange = (image) => {
    setImage(image);
    setProfileImg(image[0].data_url);
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
      <div className="add-pet-container">
        <form className="add-pet-form" onSubmit={handleSubmit}>
          <div className="edit-pet">
            <label className="pet-label">Name:</label>
            <input
              placeholder="Pet Name"
              className="pet-input"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
            />
            <label className="pet-label">Breed:</label>
            <select
              placeholder="Breed"
              className="pet-input"
              value={breed}
              onChange={(e) => setBreed(e.target.value)}
              required
            >
              <option value={breed}>{breed}</option>
              {Object.values(breeds)
                .sort(function (a, b) {
                  let nameA = a.name.toUpperCase();
                  let nameB = b.name.toUpperCase();
                  if (nameA < nameB) {
                    return -1;
                  }
                  if (nameA > nameB) {
                    return 1;
                  }
                  return 0;
                })
                .map((breed) => {
                  return <option value={breed.name}>{breed.name}</option>;
                })}
            </select>
            <label className="pet-label">Age:</label>
            <input
              placeholder="Age in years"
              className="pet-input"
              value={age}
              onChange={(e) => setAge(e.target.value)}
              required
            />
            <label className="pet-label">Profile Image:</label>
            {profile_img ? (
              <img className="upload-preview" src={profile_img} alt="upload" />
            ) : (
              <></>
            )}

            <ImageUploading
              multiple
              value={profile_img}
              onChange={onChange}
              maxNumber={1}
              dataURLKey="data_url"
            >
              {({ onImageUpload, isDragging, dragProps }) => (
                // write your building UI
                <div className="upload__image-wrapper">
                  <button
                    className="pet-button"
                    style={isDragging ? { color: "red" } : undefined}
                    onClick={onImageUpload}
                    {...dragProps}
                  >
                    Click or Drop here
                  </button>
                  &nbsp;
                </div>
              )}
            </ImageUploading>
            <label className="pet-label">Description:</label>
            <textarea
              placeholder="Post Body"
              className="pet-description-input"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              required
            />
            <button className="pet-button" type="submit">
              Submit
            </button>
          </div>
        </form>
      </div>
    </>
  );
};

export default AddPet;
