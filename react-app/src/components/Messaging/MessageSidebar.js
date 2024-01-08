import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { allMessages } from "../../store/messages";
import { getUniqueConversations } from "../utils/helperFunctions";

const MessageSidebar = ({selected, setSelected, setUserConversation}) => {
  const dispatch = useDispatch()
  const [messages, setMessages] = useState([]);
  const user = useSelector(state => state.session.user)
  const usersList = useSelector(state => state.users)
  const previousMessages = useSelector(state => state.messages)

  useEffect(() => {
    dispatch(allMessages(user.id));
  }, [dispatch, user.id]);

  useEffect(() => {
      const generatedConversations = Object.values(previousMessages).filter(
        (message) => message.user_id_to === user.id || message.user_id_from === user.id
      );
    setMessages(
      getUniqueConversations(generatedConversations, user.id)
    );
  }, [previousMessages, user.id]);

  const handleSelect = (message) => {
    if(message.user_id_from === user.id) {
      setUserConversation(message.user_id_to)
    } else {
      setUserConversation(message.user_id_from)

    }
    setSelected(!selected)
  }

  return (
    <div className='message-sidebar-container'>
      <h2>Your Converstaions:</h2>
      <div>
      {Object.values(previousMessages).length &&
            <>
            {messages.map((message, ind) => {
                return (
                  <div key={ind} onClick={() => handleSelect(message)}>
                    <img src={usersList[message.user_id_to].profile_img} />
                    <span>{`${usersList[message.user_id_to].first_name} ${
                      usersList[message.user_id_to].last_name
                    }`}</span>
                    <p>{message.lastMessage}</p>
                  </div>
                );
              })}
            </>}
      </div>
    </div>
  )
}

export default MessageSidebar