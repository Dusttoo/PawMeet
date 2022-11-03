import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { io } from 'socket.io-client';
import { allFriends } from "../../store/friends";
import './inbox.css'
let socket;

const Chat = ({setMessages, userConversation}) => {
    const dispatch = useDispatch();
    const [chatInput, setChatInput] = useState("");
    const user = useSelector(state => state.session.user)
    const usersList = useSelector(state => state.users)
    const friendsList = useSelector(state => state.friends.list)
    console.log(friendsList)
    const [sendTo, setSendTo] = useState(null)

    useEffect(() => {
        dispatch(allFriends(user.id))
        // open socket connection
        // create websocket
        socket = io();

        socket.on('data', (chat) => {
            setMessages(messages => [...messages, chat])
        })
        // when component unmounts, disconnect
        return (() => {
            socket.disconnect()
        })
    }, [])

    const updateChatInput = (e) => {
        setChatInput(e.target.value)
    };

    const sendChat = (e) => {
        e.preventDefault()
        socket.emit('data', { user_id_from: user.id, user_id_to: userConversation, msg: chatInput });
        setChatInput("")
    }

    return (user && (
        <div className="chat-container">
            <form onSubmit={sendChat}>
                <input
                    value={chatInput}
                    onChange={updateChatInput}
                />
                <button type="submit">Send</button>
            </form>
        </div>
    )
    )
};


export default Chat;