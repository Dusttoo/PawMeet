import React, { useEffect } from "react";
import { useDispatch } from "react-redux";
import { useSelector } from "react-redux";
import { useParams } from "react-router";
import { allUserAnswers } from "../../store/user_answers";
import { allBreedAnswers } from "../../store/breed_answers";
import DeleteQuiz from "./DeleteQuiz";
import PercentageCircle from "../PercentageCircle/PercentageCircle";
import { calculateResults } from "../utils/helperFunctions";
import "./Quiz.css";

const UserResults = () => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const state = useSelector((state) => state);
  const {breeds, breed_answers, user_answers, breed_images} = state;
  const results = calculateResults(breeds, breed_answers, user_answers);
  useEffect(() => {
    dispatch(allUserAnswers(id));
    dispatch(allBreedAnswers());
  }, [dispatch, id]);

  return (
    <div className="quiz-results">
      <div className="display-results-breeds">
        {results.slice(0,6).map((breed) => {
          const thisBreed = breeds[breed[0]];
          const thisImage = Object.values(breed_images).find(
            (image) => image.breed_id === thisBreed.id
          );
          if (thisImage) {
            return (
              <PercentageCircle
                image={thisImage}
                percentage={breed[1]}
                breed={thisBreed}
              />
            );
          }
        })}
      </div>
      <div className="delete-container">
        <DeleteQuiz userId={id} />
      </div>
    </div>
  );
};

export default UserResults;
