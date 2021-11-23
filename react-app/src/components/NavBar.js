
import React, { useState } from 'react';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

import './NavBar.css'
import { faUser } from '@fortawesome/free-solid-svg-icons';

const NavBar = () => {
  const currentUser = useSelector(state => state.session.user)
  return (
    <nav className='nav'>
      <ul className="nav-bar">
        <li >
          <Link className="nav-link" to='/' exact={true} activeClassName='active'>
            Home
          </Link>
        </li>
        <li >
          <Link className="nav-link" to='/forum' exact={true} activeClassName='active'>
            Speak
          </Link>
        </li>
        <li >
          <Link className="nav-link" to='/breeds' exact={true} activeClassName='active'>
            Breeds
          </Link>
        </li>
        <li >
          <Link className="nav-link" to='/breed-quiz' exact={true} activeClassName='active'>
            Breed Selector
          </Link>
        </li>
        <li>
          {currentUser ?
          <>
            <LogoutButton /> 
            <Link className='account-button' to={`/users/${currentUser.id}`} ><FontAwesomeIcon icon={faUser} /></Link>
           </>
           : <Link to='/login' className='login-button'>Log In</Link>
          }
         
        </li>
        
      </ul>
    </nav>
  );
}

export default NavBar;
