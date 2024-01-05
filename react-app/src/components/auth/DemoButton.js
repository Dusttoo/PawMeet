import React from "react";
import * as sessionActions from "../../store/session";
import { useDispatch } from "react-redux";
import "./Auth.css";

const DemoButton = () => {
  const dispatch = useDispatch();
  const handleSubmit = (e) => {
    e.preventDefault();
    return dispatch(sessionActions.login("demo@aa.io", "password"));
  };

  return (
    <>
      <button className="login-button" onClick={handleSubmit}>
        Demo User
      </button>
    </>
  );
};

export default DemoButton;
