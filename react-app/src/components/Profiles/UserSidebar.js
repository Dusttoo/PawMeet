import React from "react";
import { Link, useParams } from "react-router-dom";
import "./Profiles.css";

const UserSidebar = () => {
  const { id } = useParams();
  return (
    <>
      <div className="user-side-container">
        <h1>sidebar</h1>
        <Link to={`/friends/${id}`}>friends list</Link>
        <Link to={`/requests/${id}`}>friend requests</Link>
      </div>
    </>
  );
};

export default UserSidebar;
