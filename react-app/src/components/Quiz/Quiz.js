import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { useSelector } from "react-redux";
import { allBreedTraits } from "../../store/breed_traits";
import "./Quiz.css";
import DisplayQuestion from "./DisplayQuestion";
import UserResults from "./QuizResults";
import Loading from "../Loading/Loading";
import { allUserAnswers } from "../../store/user_answers";

const Quiz = () => {
  const dispatch = useDispatch();
  const userAnswers = useSelector((state) => state.user_answers);
  const currentUser = useSelector((state) => state.session.user);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    dispatch(allBreedTraits());
    dispatch(allUserAnswers(currentUser.id));
    setLoading(false);
  }, [dispatch]);

  return (
    <div className="quiz-container">
      {loading ? (
        <>
          <Loading />
        </>
      ) : (
        <>
          {Object.keys(userAnswers).length >= 16 ? (
            <>
              <div className="results-page-container">
                <h1 className="matches-title">Your Matches</h1>
                <UserResults />
              </div>
            </>
          ) : (
            <>
              <div className="number-container">
                <p className="question-number">
                  Question <span className="current-number">{Object.keys(userAnswers).length + 1}</span>/16
                </p>
              </div>
              <DisplayQuestion />
            </>
          )}
        </>
      )}
    </div>
  );
};

export default Quiz;
