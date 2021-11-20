import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect, Link } from 'react-router-dom';
import { login } from '../../store/session';
import './Auth.css'
import DemoButton from './DemoButton';


const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/' />;
  }

  return (
  <div className='login-container' style={{backgroundImage:'url("https://assets-global.website-files.com/5ef2757ec474d80aea09a025/5fbe798b8763824ba303bbc3_petplan-help-dog-og.jpg")'}}>
    <form className='login-form' onSubmit={onLogin}>
      {/* <div>
        {errors.map((error, ind) => (
          <div key={ind}>{error}</div>
        ))}
      </div> */}
      <div className='row'>
        <div>
        {errors.map((error, ind) => {
         const where = error.slice(0, error.indexOf(':'))
          const onlyError = error.slice(error.indexOf(':') + 1)
          if(where.includes('email')) {

            return (
              <div className='error' key={ind}>{onlyError}</div>
            )
          }
          
        })}
        </div>
        <label className='label' htmlFor='email'>Email:</label>
        <input
          className='input'
          name='email'
          type='text'
          placeholder='Email'
          value={email}
          onChange={updateEmail}
        />
      </div>
      <div className='row'>
        <div>
        {errors.map((error, ind) => {
          const where = error.slice(0, error.indexOf(':'))
          const onlyError = error.slice(error.indexOf(':') + 1)
          if(where.includes('password')) {

            return (
              <div className='error' key={ind}>{onlyError}</div>
            )
          }
          
          
        })}
        </div>
        <label className='label' htmlFor='password'>Password:</label>
        <input
          className='input'
          name='password'
          type='password'
          placeholder='Password'
          value={password}
          onChange={updatePassword}
        />
      </div>
      <div className='login-submit-container'>
        <button className='login-button' type='submit'>Login</button>
        <DemoButton />
      </div>
      <p className='already'>Don't have an account? <Link className='login-redirect' to='/sign-up'>Sign Up</Link></p>
      <h3 className='login-slogan'>Let the barking begin</h3>

    </form>
    
  </div>  
  );
};

export default LoginForm;
