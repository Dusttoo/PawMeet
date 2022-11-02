import React, { useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import "./Profiles.css";
import { allFriends, allRequests } from "../../store/friends";

const FriendRequests = () => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const requests = useSelector((state) => state.friends.requests);
  const users = useSelector((state) => state.users);
  const currentUser = useSelector((state) => state.session.user.id);
  const sent = [];
  const recieved = [];

  useEffect(() => {
    dispatch(allRequests(id));
  }, []);

  Object.values(requests).map((request) => {
    const request_user = request.user_id_from;
    console.log(request_user, currentUser);
    if (request_user === currentUser) {
      sent.push(request_user);
    } else {
      console.log(request_user);
      recieved.push(request_user);
    }
  });
  console.log(sent, recieved);

  return (
    <>
      <div className="firends-list-container">
        <h1>Requests</h1>
        <h2>Your sent requests:</h2>
        {sent.length ? (
          <>
            {Object.values(sent).map((id) => {
              console.log(id);
              return (
                <>
                  <p>{users[id].first_name}</p>
                </>
              );
            })}
          </>
        ) : (
          <p>No sent requests</p>
        )}
        <h2>Your received requests</h2>
        {recieved.length ? (
          <>
            {Object.values(recieved).map((id) => {
              const friend = users[id];
              return (
                <>
                  <img src={friend.profile_img} alt={friend.first_name} />
                  <p>
                    {friend.first_name} {friend.last_name}
                  </p>
                </>
              );
            })}
          </>
        ) : (
          <p>No sent requests</p>
        )}
      </div>
    </>
  );
};

export default FriendRequests;
