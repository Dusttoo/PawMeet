
import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import './NavBar.css'

const NavBar = () => {
  return (
    <nav >
      <ul className="nav-bar">
        <li >
          <NavLink className="nav-link" to='/' exact={true} activeClassName='active'>
            Home
          </NavLink>
        </li>
        <li >
          <NavLink className="nav-link" to='/login' exact={true} activeClassName='active'>
            Login
          </NavLink>
        </li>
        <li >
          <NavLink className="nav-link" to='/sign-up' exact={true} activeClassName='active'>
            Sign Up
          </NavLink>
        </li>
        <li >
          <NavLink className="nav-link" to='/users' exact={true} activeClassName='active'>
            Users
          </NavLink>
        </li>
        <li >
          <NavLink className="nav-link" to='/forum' exact={true} activeClassName='active'>
            Forum
          </NavLink>
        </li>
        <li>
          <LogoutButton />
        </li>
      </ul>
    </nav>
  );
}

export default NavBar;
