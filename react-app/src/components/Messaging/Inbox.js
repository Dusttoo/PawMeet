import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { allMessages } from "../../store/messages";
import Chat from './Socket'
import MessageSidebar from './MessageSidebar'
import './inbox.css'

const Inbox = () => {
  const dispatch = useDispatch()
  const [messages, setMessages] = useState([]);
  const [selected, setSelected] = useState(false)
  const [userConversation, setUserConversation] = useState(null)
  const user = useSelector(state => state.session.user)
  const usersList = useSelector(state => state.users)
  const previousMessages = useSelector(state => state.messages)
  console.log(previousMessages)

  useEffect(() => {
    dispatch(allMessages(user.id))
  }, [])

  return (
    <div className='inbox-page-container'>
    <MessageSidebar selected={selected} setSelected={setSelected} setUserConversation={setUserConversation}/>
    <div className='message-details-container'>
        <div className='inbox-header'>Inbox</div>
        {selected ?
        <>
        <div className=''>Your chat with:
        </div>
        <div>
            {Object.values(previousMessages).length &&
            <>
            {Object.values(previousMessages).map((message, ind) => (
              
              <div key={ind}>{`${usersList[message.user_id_from].first_name}: ${message.message}`}</div>
            ))}
            </>}
            {messages.map((message, ind) => {
              if(!Object.values(previousMessages).includes(message.data)) {
                return (
                  <>
                    <div key={ind}>{`${usersList[message.data.user_id_from].first_name}: ${message.data.msg}`}</div>
                  </> 
                  )
              }
              })}
        </div>
        </> : 
        <p>put something here</p>
      }
        
    </div>
    <Chat setMessages={setMessages} selected={selected} userConversation={userConversation}/>
    </div>
  )
}

export default Inbox