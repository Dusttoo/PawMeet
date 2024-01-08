import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { io } from "socket.io-client";
import { allFriends } from "../../store/friends";
import "./inbox.css";
let socket;

const Chat = ({ setNewMessages, sendTo }) => {
  const dispatch = useDispatch();
  const [chatInput, setChatInput] = useState("");
  const user = useSelector((state) => state.session.user);
  const usersList = useSelector((state) => state.users);
  const friendsList = useSelector((state) => state.friends.list);

  useEffect(() => {
    dispatch(allFriends(user.id));
    socket = io();

    socket.on("data", (chat) => {
      setNewMessages((currentMessages) => [...currentMessages, chat.data]);
    });
    return () => {
      socket.disconnect();
    };
  }, [setNewMessages, user.id, dispatch]);

  const updateChatInput = (e) => {
    setChatInput(e.target.value);
  };

  const sendChat = (e) => {
    e.preventDefault();
    if (sendTo && chatInput.trim()) {
      socket.emit("data", {
        user_id_from: user.id,
        user_id_to: sendTo,
        message: chatInput,
      });
      setChatInput("");
    }
  };

  return (
    user && (
      <div className="chat-container">
        <form onSubmit={sendChat}>
          <input value={chatInput} onChange={updateChatInput} />
          <button type="submit">Send</button>
        </form>
      </div>
    )
  );
};

export default Chat;
