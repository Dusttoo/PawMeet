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
import { allBreeds } from './store/breeds';
import { allGroups } from './store/breed_groups';
import BreedsPage from './components/Breeds/Breeds';
import BreedInfo from './components/Breeds/BreedInfo';
import { allImages } from './store/breed_images';
import BreedForum from './components/Forum/BreedForum';
import Landing from './components/Landing/Landing';


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
      await dispatch(allBreeds())
      await dispatch(allGroups())
      await dispatch(allImages())
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
        <ProtectedRoute path='/forum/add' exact={true} >
          <AddPost />
        </ProtectedRoute>
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
        <Route path='/breeds' exact={true} >
          <BreedsPage />
        </Route>
        <Route path='/breeds/:id' exact={true} >
          <BreedInfo />
        </Route>
        <Route path='/breeds/group/:id' exact={true} >
          <h1>Group page</h1>
        </Route>
        <Route path='/forum' exact={true} >
          <ForumHome />
        </Route>
        <Route path='/forum/:id' exact={true} >
          <BreedForum />
        </Route>
        <Route path='/forum/posts/:postId' exact={true} >
          <Posts />
        </Route>
        <Route path='/' exact={true} >
          <Landing />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
