import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect } from 'react-router-dom';
import { signUp } from '../../store/session';
import { Link } from 'react-router-dom';
import DemoButton from './DemoButton';

const SignUpForm = () => {
  const [errors, setErrors] = useState([]);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');
  const [first_name, setFirstName] = useState('')
  const [last_name, setLastName] = useState('')
  const [profile_img, setProfileImg] = useState('')
  const barking_since = new Date();
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  console.log('username', username, 'email', email, 'password',password, 'repeatPassword',repeatPassword, 'first_name',first_name, 'last_name',last_name, 'profile_img',profile_img, 'barking_since',barking_since)

  const onSignUp = async (e) => {
    e.preventDefault();
      const data = await dispatch(signUp(username, email, password, first_name, last_name, profile_img, barking_since));
      if (data) {
        setErrors(data)
    }
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  const updateFirstName= (e) => {
    setFirstName(e.target.value);
  };
  const updateLastName= (e) => {
    setLastName(e.target.value);
  };
  const updateProfileImg= (e) => {
    setProfileImg(e.target.value);
  };

  if (user) {
    return <Redirect to='/' />;
  }


  return (
  <div className='login-container' style={{backgroundImage:'url("https://assets-global.website-files.com/5eec3c1c4f68093fae5f1f37/6036c672b7d1065cbc3986da_pug-ate-chocolate.jpg")'}}>
    <form className='login-form' onSubmit={onSignUp}>
      {/* <div>
        {errors.map((error, ind) => (
          <div className='error' key={ind}>{error}</div>
        ))}
      </div> */}
      <div className='row'>
        <div>
        {errors.map((error, ind) => {
          const where = error.slice(0, error.indexOf(':'))
          const onlyError = error.slice(error.indexOf(':') + 1)
          if(where.includes('username')) {

            return (
              <div className='error' key={ind}>{onlyError}</div>
            )
          }
          
        })}
        </div>
        <label className='label' >User Name</label>
        <input
          className='input'
          type='text'
          name='username'
          onChange={updateUsername}
          value={username}
        ></input>
      </div>
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
        <label className='label'>Email</label>
        <input
          className='input'
          type='text'
          name='email'
          onChange={updateEmail}
          value={email}
        ></input>
        <label className='label'>First Name</label>
        <input
          className='input'
          type='text'
          name='firstName'
          onChange={updateFirstName}
          value={first_name}
        ></input>
        <label className='label'>Last Name</label>
        <input
          className='input'
          type='text'
          name='lastName'
          onChange={updateLastName}
          value={last_name}
        ></input>
        <label className='label'>Profile Image</label>
        <input
          className='input'
          type='text'
          name='profileImg'
          onChange={updateProfileImg}
          value={profile_img}
        ></input>
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
        
        <label className='label'>Password</label>
        <input
          className='input'
          type='password'
          name='password'
          onChange={updatePassword}
          value={password}
        ></input>
      </div>
      <div className='row'>
        <label className='label'>Repeat Password</label>
        <input
          className='input'
          type='password'
          name='repeat_password'
          onChange={updateRepeatPassword}
          value={repeatPassword}
          // required={true}
        ></input>
      </div>
      <div className='login-submit-container'>
        <button className='login-button' type='submit'>Sign Up</button>
        <DemoButton />
      </div>
      <p className='already'>Already a user? <Link className='login-redirect' to='/login'>Log In</Link></p>
      <h3 className='login-slogan'>See what all the barking's about!</h3>
    </form>
  </div>
  );
};

export default SignUpForm;
