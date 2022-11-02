import React, { useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import "./Profiles.css";
import { allFriends } from "../../store/friends";

const FriendsList = () => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const friendsList = useSelector((state) => state.friends.list);
  const users = useSelector((state) => state.users);
  console.log("list", friendsList);

  useEffect(() => {
    dispatch(allFriends(id));
  }, [id]);

  return (
    <>
      <div className="firends-list-container">
        <h1>Friends</h1>
        {Object.values(friendsList).map((connection) => {
          console.log(connection);
          const friendId = connection.friend_user_id;
          const friend = users[friendId];
          console.log(friend);
          return (
            <>
              <div key={connection.id} className="friend-container">
                <img
                  className="friend-image"
                  src={friend.profile_img}
                  alt={friend.first_name}
                />
                <p>
                  {friend.first_name} {friend.last_name}
                </p>
              </div>
            </>
          );
        })}
      </div>
    </>
  );
};

export default FriendsList;
