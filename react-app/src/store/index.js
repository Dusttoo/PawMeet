import { createStore, combineReducers, applyMiddleware, compose } from "redux";
import thunk from "redux-thunk";
import session from "./session";
import forumReducer from "./forum";
import usersReducer from "./users";
import commentReducer from "./comments";
import post_commentReducer from "./post_comments";
import likeReducer from "./likes";
import petReducer from "./pets";
import breedReducer from "./breeds";
import groupReducer from "./breed_groups";
import imageReducer from "./breed_images";
import breedTraitReducer from "./breed_traits";
import breedAnswerReducer from "./breed_answers";
import groupPostReducer from "./group_posts";
import userAnswerReducer from "./user_answers";
import friendReducer from "./friends";
import messageReducer from "./messages";

const rootReducer = combineReducers({
  session,
  forum: forumReducer,
  users: usersReducer,
  comments: commentReducer,
  post_comments: post_commentReducer,
  likes: likeReducer,
  pets: petReducer,
  breeds: breedReducer,
  groups: groupReducer,
  breed_images: imageReducer,
  breed_traits: breedTraitReducer,
  breed_answers: breedAnswerReducer,
  group_posts: groupPostReducer,
  user_answers: userAnswerReducer,
  friends: friendReducer,
  messages: messageReducer,
});

let enhancer;

if (process.env.NODE_ENV === "production") {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = require("redux-logger").default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
