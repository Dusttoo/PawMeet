import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "./UsersList.css";

function UsersList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch("/api/users/");
      const responseData = await response.json();
      setUsers(responseData.users);
    }
    fetchData();
  }, []);

  const userComponents = users.map((user) => {
    return (
      <div className="user">
        <Link to={`/users/${user.id}`}>
          <img
            className="user-icon"
            src={user.profile_img}
            alt={user.first_name}
          />
        </Link>
        <Link className="user-name" to={`/users/${user.id}`}>
          {user.first_name}
        </Link>
      </div>
    );
  });

  return (
    <div className="users-container">
      <h1>User List: </h1>
      <div className="users-list">{userComponents}</div>
    </div>
  );
}

export default UsersList;
