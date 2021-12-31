import React from "react";
import { useDispatch } from "react-redux";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { removeAnswer } from "../../store/user_answers";
import { useHistory } from "react-router";
import { faRotateLeft } from "@fortawesome/free-solid-svg-icons";
import "./Quiz.css";
import scrollToTop from "../utils/scroll";

const DeleteQuiz = ({ userId }) => {
  const dispatch = useDispatch();
  const history = useHistory();

  const deleteQuiz = () => {
    dispatch(removeAnswer(userId));
    history.push(`/breed-quiz/${userId}`);
    scrollToTop();
  };

  return (
    <>
      <button className="delete-quiz" onClick={deleteQuiz}>
        Start over
        <FontAwesomeIcon className="restart-icon" icon={faRotateLeft} />
      </button>
    </>
  );
};

export default DeleteQuiz;
