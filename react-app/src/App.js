import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import NavBar from './components/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import User from './components/User';
import { authenticate } from './store/session';
import ForumHome from './components/Forum/Forum_Main';
import Header from './components/Header/Header';
import { allUsers } from './store/users';
import { allPosts} from './store/forum';
import { allComments } from './store/comments';
import Posts from './components/Forum/Post';
import UserProfile from './components/Profiles/UserProfile';
import AddPost from './components/Forum/AddPost';
import { allLikes } from './store/likes';
import { allPets } from './store/pets';
import PetProfile from './components/Profiles/PetProfile';
import AddPet from './components/Profiles/addPet';


function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      await dispatch(allUsers())
      await dispatch(allPosts())
      await dispatch(allLikes())
      await dispatch(allPets())

      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <Header />
      <NavBar />
      <Switch>
        <Route path='/login' exact={true}>
          <LoginForm />
        </Route>
        <Route path='/sign-up' exact={true}>
          <SignUpForm />
        </Route>
        <ProtectedRoute path='/users' exact={true} >
          <UsersList/>
        </ProtectedRoute>
        <ProtectedRoute path='/users/:id' exact={true} >
          <UserProfile/>
        </ProtectedRoute>
        <ProtectedRoute path='/pets/add' exact={true} >
          <AddPet />
        </ProtectedRoute>
        <ProtectedRoute path='/pets/:id' exact={true} >
          <PetProfile />
        </ProtectedRoute>
        <ProtectedRoute path='/forum' exact={true} >
          <ForumHome />
        </ProtectedRoute>
        <ProtectedRoute path='/forum/add' exact={true} >
          <AddPost />
        </ProtectedRoute>
        <ProtectedRoute path='/forum/posts/:postId' exact={true} >
          <Posts />
        </ProtectedRoute>
        <ProtectedRoute path='/' exact={true} >
          <h1>My Home Page</h1>
        </ProtectedRoute>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
