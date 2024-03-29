import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { editAPet } from "../../store/pets";
import { useHistory } from "react-router";
import { sortBreedsByName } from "../utils/helperFunctions";
import "./Profiles.css";

const EditPet = ({ openEditForm }) => {
  const { id } = useParams();
  const [validationErrors, setValidationErrors] = useState([]);
  const dispatch = useDispatch();
  const breeds = useSelector((state) => state.breeds);
  const pets = useSelector((state) => state.pets);
  const [profile_img, setProfileImg] = useState(pets[id].profile_img);
  const [name, setName] = useState(pets[id].name);
  const [breed, setBreed] = useState(pets[id].breed);
  const [age, setAge] = useState(pets[id].age);
  const [description, setDescription] = useState(pets[id].description);
  const owner_id = useSelector((state) => state.session.user.id);
  const history = useHistory();

  const validate = () => {
    const validationErrors = [];
    if (!name) validationErrors.push("Name is required");
    if (name.length < 3)
      validationErrors.push("Name must be at least 3 characters");
    if (!breed) validationErrors.push("Please select a breed");
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
      const added = await dispatch(editAPet(createdPet, +id));
      if (added) {
        openEditForm();
        history.push(`/pets/${id}`);
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
              {sortBreedsByName(Object.values(breeds)).map((breed) => {
                return <option value={breed.name}>{breed.name}</option>;
              })}
            </select>
            <label className="pet-label">Age:</label>
            <input
              placeholder="Age in years"
              className="pet-input"
              type="number"
              value={age}
              onChange={(e) => setAge(e.target.value)}
              required
            />
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

export default EditPet;
