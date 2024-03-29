import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { useDispatch } from "react-redux";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import UsersList from "./components/UsersList";
import { authenticate } from "./store/session";
import ForumHome from "./components/Forum/Forum_Main";
import Header from "./components/Header/Header";
import { allUsers } from "./store/users";
import { allPosts } from "./store/forum";
import Posts from "./components/Forum/Post";
import UserProfile from "./components/Profiles/UserProfile";
import AddPost from "./components/Forum/AddPost";
import { allLikes } from "./store/likes";
import { allPets } from "./store/pets";
import PetProfile from "./components/Profiles/PetProfile";
import AddPet from "./components/Profiles/addPet";
import { allBreeds } from "./store/breeds";
import { allGroups } from "./store/breed_groups";
import BreedsPage from "./components/Breeds/Breeds";
import BreedInfo from "./components/Breeds/BreedInfo";
import { allImages } from "./store/breed_images";
import BreedForum from "./components/Forum/BreedForum";
import Landing from "./components/Landing/Landing";
import Footer from "./components/Footer/Footer";
import UserResults from "./components/Quiz/QuizResults";
import Quiz from "./components/Quiz/Quiz";
import { allBreedTraits } from "./store/breed_traits";
import FriendsList from "./components/Profiles/FriendsList";
import FriendRequests from "./components/Profiles/FriendRequests";
import Inbox from "./components/Messaging/Inbox";

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      await dispatch(allUsers());
      await dispatch(allPosts());
      await dispatch(allLikes());
      await dispatch(allPets());
      await dispatch(allBreeds());
      await dispatch(allGroups());
      await dispatch(allImages());
      await dispatch(allBreedTraits());
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
        <Route path="/login" exact={true}>
          <LoginForm />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm />
        </Route>
        <ProtectedRoute path="/forum/add" exact={true}>
          <AddPost />
        </ProtectedRoute>
        <ProtectedRoute path="/users" exact={true}>
          <UsersList />
        </ProtectedRoute>
        <ProtectedRoute path="/users/:id" exact={true}>
          <UserProfile />
        </ProtectedRoute>
        <ProtectedRoute path="/friends/:id" exact={true}>
          <FriendsList />
        </ProtectedRoute>
        <ProtectedRoute path="/requests/:id" exact={true}>
          <FriendRequests />
        </ProtectedRoute>
        <ProtectedRoute path="/pets/add" exact={true}>
          <AddPet />
        </ProtectedRoute>
        <ProtectedRoute path="/pets/:id" exact={true}>
          <PetProfile />
        </ProtectedRoute>
        <ProtectedRoute path="/quiz-results/:id" exact={true}>
          <UserResults />
        </ProtectedRoute>
        <ProtectedRoute path="/breed-quiz/:id" exact={true}>
          <Quiz />
        </ProtectedRoute>
        <Route path="/breeds" exact={true}>
          <BreedsPage />
        </Route>
        <Route path="/breeds/:id" exact={true}>
          <BreedInfo />
        </Route>
        <Route path="/breeds/group/:id" exact={true}>
          <h1>Group page</h1>
        </Route>
        <Route path="/forum" exact={true}>
          <ForumHome />
        </Route>
        <Route path="/forum/:id" exact={true}>
          <BreedForum />
        </Route>
        <ProtectedRoute path="/forum/posts/:postId" exact={true}>
          <Posts />
        </ProtectedRoute>
        <Route path="/inbox/:id" exact={true}>
          <Inbox />
        </Route>
        <Route path="/" exact={true}>
          <Landing />
        </Route>
      </Switch>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
