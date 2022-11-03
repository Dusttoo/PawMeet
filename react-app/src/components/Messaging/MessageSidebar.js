import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { allMessages } from "../../store/messages";
import {v4 as uuidv4} from 'uuid';

const MessageSidebar = ({selected, setSelected, setUserConversation}) => {
  const dispatch = useDispatch()
  const [messages, setMessages] = useState([]);
  const user = useSelector(state => state.session.user)
  const usersList = useSelector(state => state.users)
  const previousMessages = useSelector(state => state.messages)
  const generatedConversations = []
  console.log(generatedConversations.includes({'to': 2, 'from': 1}), {'to': 2, 'from': 1} in generatedConversations)

  useEffect(() => {
    dispatch(allMessages(user.id))
  }, [])

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
            {Object.values(previousMessages).map((message, ind) => {
              
              if(!generatedConversations.includes({'to': message.user_id_from, 'from': message.user_id_to})) {
                generatedConversations.push({'to': message.user_id_to, 'from': message.user_id_from})
                generatedConversations.push({'to': message.user_id_from, 'from': message.user_id_to})
                return (
                  <div 
                  key={ind}
                  onClick={() => handleSelect(message)}>
                    <img src='' />
                    <span>{`${usersList[message.user_id_from].first_name} ${usersList[message.user_id_from].last_name}`}</span>
                    <p>{message.message}</p>
                    </div>
                  )
              }
              
              })}
            </>}
      </div>
    </div>
  )
}

export default MessageSidebar