import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { allMessages } from "../../store/messages";
import Chat from "./Socket";
import MessageSidebar from "./MessageSidebar";
import SelectUserDropdown from "./SelectUserDropDown";
import "./inbox.css";

const Inbox = () => {
  const dispatch = useDispatch();
  const [messages, setMessages] = useState([]);
  const [newMessages, setNewMessages] = useState([]);
  const [selected, setSelected] = useState(false);
  const [userConversation, setUserConversation] = useState(null);
  const user = useSelector((state) => state.session.user);
  const usersList = useSelector((state) => state.users);
  const previousMessages = useSelector((state) => state.messages);

  useEffect(() => {
    dispatch(allMessages(user.id));
  }, [dispatch, user.id]);

  useEffect(() => {
    setMessages([...Object.values(previousMessages), ...newMessages]);
  }, [previousMessages, newMessages]);

  const handleUserSelect = (userId) => {
    setUserConversation(userId);
    setSelected(true);
  };

  return (
    <div className="inbox-page-container">
      <MessageSidebar
        selected={selected}
        setSelected={setSelected}
        setUserConversation={setUserConversation}
      />
      <div className="message-details-container">
        <div className="inbox-header">Inbox</div>
        {selected ? (
          <>
            <div className="">
              Your chat with: {usersList[userConversation].first_name}
            </div>
            <div>
              {messages.length && (
                <>
                  {messages.map((message, ind) => {
                    if (
                      parseInt(userConversation) === message.user_id_from ||
                      parseInt(userConversation) === message.user_id_to
                    ) {
                      return (
                        <div key={ind}>{`${
                          usersList[message.user_id_from].first_name
                        }: ${message.message}`}</div>
                      );
                    }
                  })}
                </>
              )}
            </div>
          </>
        ) : (
          <SelectUserDropdown onSelect={handleUserSelect} />
        )}
      </div>
      <Chat
        setNewMessages={setNewMessages}
        selected={selected}
        sendTo={userConversation}
      />
    </div>
  );
};

export default Inbox;
