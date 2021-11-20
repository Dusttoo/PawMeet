import React, { useState } from 'react';
import * as sessionActions from "../../store/session";
import { useSelector, useDispatch } from 'react-redux';
import { Redirect } from 'react-router-dom';
import { Link } from 'react-router-dom'
import { login } from '../../store/session';
import './Auth.css'

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