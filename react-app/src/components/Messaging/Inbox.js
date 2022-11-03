import React, { useState } from "react";
import { useSelector } from "react-redux";


import Chat from './Socket'
import MessageSidebar from './MessageSidebar'
import './inbox.css'

const Inbox = () => {
  const [messages, setMessages] = useState([]);
  const user = useSelector(state => state.session.user)
  const usersList = useSelector(state => state.users)
    console.log(messages)

  return (
    <div className='inbox-page-container'>
    <MessageSidebar />
    <div className='message-details-container'>
        <div className='inbox-header'>Inbox</div>
        <div className=''>Your chat with: {
        messages.length &&
        messages[0].from !== user.id ? usersList[messages[0].from].firstName :
        usersList[messages[0].from].lastName}</div>
        <div>
            {messages.map((message, ind) => (
                <div key={ind}>{`${usersList[message.from]}: ${message.msg}`}</div>
            ))}
        </div>
    </div>
    <Chat setMessages={setMessages}/>
    </div>
  )
}

export default Inbox