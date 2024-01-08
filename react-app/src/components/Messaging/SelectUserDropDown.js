// SelectUserDropdown.js

import React from "react";
import { useSelector } from "react-redux";

const SelectUserDropdown = ({ onSelect }) => {
  const usersList = useSelector((state) => state.users);
  const friendsList = useSelector((state) => state.friends.list);

  const handleSelect = (event) => {
    onSelect(event.target.value);
  };

  return (
    <select onChange={handleSelect} defaultValue="">
      <option value="" disabled>
        Select a friend
      </option>
      {Object.values(friendsList).map((friend) => (
        <option key={friend.friend_user_id} value={friend.friend_user_id}>
          {usersList[friend.friend_user_id].first_name}{" "}
          {usersList[friend.friend_user_id].last_name}
        </option>
      ))}
    </select>
  );
};

export default SelectUserDropdown;
