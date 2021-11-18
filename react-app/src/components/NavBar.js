
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
