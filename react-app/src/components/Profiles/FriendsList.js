import React, { useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import "./Profiles.css";
import { allFriends } from "../../store/friends";

const FriendsList = () => {
  const { id } = useParams();
  const dispatch = useDispatch()
  const friendsList = useSelector(state => state.friends.list)
  const users = useSelector(state => state.users)
  

  useEffect(() => {
    dispatch(allFriends(id))
  }, [])

  return (
    <>
      <div className="firends-list-container">
        <h1>Friends</h1>
        {Object.values(friendsList).map(connection => {
            const friendId = connection.friend_user_id
            const friend = users[friendId]
            console.log(friend)
            return (
                <>
                <img src={friend.profile_img} alt={friend.first_name}/>
                <p>{friend.first_name} {friend.last_name}</p>
                </>
            )
        })}
      </div>
    </>
  );
};

export default FriendsList;
