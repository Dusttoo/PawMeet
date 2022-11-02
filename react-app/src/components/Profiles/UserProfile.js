import React from "react";
import { useSelector } from "react-redux";
import { Link, useParams } from "react-router-dom";
import DisplayPosts from "../Forum/DisplayPost";
import { getFivePosts,  modifyTime} from "../utils/helperFunctions";
import "./Profiles.css";

const UserProfile = () => {
  const { id } = useParams();
  const state = useSelector((state) => state);
  const {users, session, pets, forum} = state;
  const userPets =  Object.values(pets).filter((pet) => +pet.owner_id === +id);

  return (
    <>
      <div className="user-page">
        <div className="user-container">
          <div className="user-header">
            <img
              className="profile-img"
              src={users[id].profile_img}
              alt={users[id].first_name}
            ></img>
            <div className="user-details-header">
              <h1>
                {users[id].first_name} {users[id].last_name}
              </h1>
              <p>Barking since: {modifyTime(users[id].barking_since)}</p>
            </div>
          </div>
          <div className="user-content">
            <div className="pet-links">
              <h3>Pets:</h3>
              <div className="pet-links-container">
                {!userPets.length ? <h2>No pets to display.</h2> : <></>}
                {userPets.map((pet) => {
                  return (
                    <Link className="pet-link" to={`/pets/${pet.id}`}>
                      <div className="pet-link-details">
                        <img
                          className="pet-link-image"
                          src={pet.profile_img}
                          alt={pet.name}
                        />
                        <p className="pet-link-name">{pet.name}</p>
                      </div>
                    </Link>
                  );
                })}
              </div>
            </div>
            <div className="user-posts">
              <h3>Recent Posts:</h3>
              <div className="user-post-list">
                {getFivePosts(Object.values(forum)).map((post) => {
                  return <DisplayPosts post={post} />;
                })}
              </div>
            </div>
          </div>
          {+id === session.user.id && (
            <Link className="add-pet" to="/pets/add">
              Add a pet
            </Link>
          )}
        </div>
      </div>
    </>
  );
};

export default UserProfile;
