import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useSelector } from "react-redux";
import "./Quiz.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faRightLong } from "@fortawesome/free-solid-svg-icons";
import { addAnAnswer } from "../../store/user_answers";
import GifPlayer from "react-gif-player";
import scrollToTop from "../utils/scroll";
import { faPaw } from "@fortawesome/free-solid-svg-icons";

const DisplayQuestion = () => {
  const [validationErrors, setValidationErrors] = useState([]);
  const dispatch = useDispatch();
  const [answer, setAnswer] = useState("");
  const [isChecked, setIsChecked] = useState(false);
  const [next, setNext] = useState(1);
  const [check, setCheck] = useState(false);
  const breedTraits = useSelector((state) => state?.breed_traits);
  const trait_id = breedTraits[next].id;
  const breeds = useSelector((state) => state?.breeds);
  const user_id = useSelector((state) => state.session.user.id);
  const normal = [7,8]
  const coatTypes = [
    "Wiry",
    "Rough",
    "Curly",
    "Hairless",
    "Corded",
    "Wavy",
    "Smooth",
    "Double",
    "Silky",
  ];
  let index = 0;
  const coatLengths = ["Short", "Medium", "Long"];
  const breedImages = useSelector((state) => state.breed_images);
  const [loading, setLoading] = useState(false);
  const [img, setImg] = useState(breedImages[1].img_url);

  const imageSet = () => {
    const min = 1;
    const max = Object.keys(breeds).length;
    const num = Math.floor(Math.random() * (max - min) + min);
    const thisImg = Object.values(breedImages)[num];
    setImg(thisImg.img_url);
  };

  const validate = () => {
    if (!answer) {
      validationErrors.push("Please choose an answer.");
    }
    return validationErrors;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const createdAnswer = {
      user_id,
      trait_id,
      answer: +answer,
      important: isChecked,
    };
    const errors = validate();
    if (errors.length > 0) {
      setValidationErrors(errors);
    } else {
      setValidationErrors([]);
      const added = await dispatch(addAnAnswer(createdAnswer));
      if (added) {
      }
    }
    setNext(next + 1);
    imageSet();
    setLoading(false);
    setAnswer("");
    setIsChecked(false);
    scrollToTop();
  };

  const checkAnswer = () => {
    if (!answer) {
      setCheck(true);
    } else {
      setCheck(false);
    }
  };

  const checkBox = () => {
    setIsChecked(!isChecked);
  };

  return (
    <div className="question-quiz-container">
      {loading ? (
        <>
          <div className="loading-container">
            <GifPlayer gif="https://i.imgur.com/JS8bT2R.gif" autoplay={true} />
            <h2 className="highlighted-breed-name">Calling all the dogs...</h2>
          </div>
        </>
      ) : (
        <>
          <div className="image-container">
            <img className="quiz-image" src={img} alt="breed quiz"></img>
            <h2 className="question">{breedTraits[next].question}</h2>
          </div>
          {check && <p className="error">Please choose an answer</p>}
          <div className="add-form-container">
            <form className="post-form" onSubmit={handleSubmit}>
              <div className="quiz-form-con">
                <div className="coat-container">
                  {breedTraits[next].id === 7 && (
                    <>
                      {coatTypes.map((coat) => {
                        index++;
                        return (
                          <>
                            <div className="coat-box">
                              <label className="coat-radio-title">{coat}</label>
                              <div className="coat-min-max">
                                <label className="container">
                                  <input
                                    type="radio"
                                    name="type"
                                    className="quiz-radio"
                                    value={index}
                                    onChange={(e) => setAnswer(e.target.value)}
                                    required
                                  />
                                  <FontAwesomeIcon
                                    className="paw"
                                    icon={faPaw}
                                  />
                                </label>
                              </div>
                            </div>
                          </>
                        );
                      })}
                    </>
                  )}
                  {breedTraits[next].id === 8 && (
                    <>
                      {coatLengths.map((coat) => {
                        index++;
                        return (
                          <div className="coat-box">
                            <label className="coat-radio-title">{coat}</label>
                            <div className="coat-min-max">
                              <label className="container">
                                <input
                                  type="radio"
                                  name="length"
                                  className="quiz-radio"
                                  value={index}
                                  onChange={(e) => setAnswer(e.target.value)}
                                  required
                                />
                                <FontAwesomeIcon className="paw" icon={faPaw} />
                              </label>
                            </div>
                          </div>
                        );
                      })}
                    </>
                  )}
                  {!normal.includes(breedTraits[next].id) && (
                    // Could split this into another component for readability
                    <div className="regular-questions">
                      <div className="amount-labels">
                        <label className="radio-title">
                          {breedTraits[next].min}
                        </label>
                        <label className="radio-title">
                          {breedTraits[next].max}
                        </label>
                      </div>
                      <div className="response-container">
                        <div className="min-max">
                          <label className="container">
                            <input
                              type="radio"
                              name="answer"
                              className="quiz-radio"
                              value={1}
                              onChange={(e) => setAnswer(e.target.value)}
                              required
                            />
                            <FontAwesomeIcon className="paw" icon={faPaw} />
                          </label>
                        </div>
                        <div className="min-max">
                          <label className="container">
                            <input
                              type="radio"
                              className="quiz-radio"
                              name="answer"
                              value={2}
                              onChange={(e) => setAnswer(e.target.value)}
                              required
                            />
                            <FontAwesomeIcon className="paw" icon={faPaw} />
                          </label>
                        </div>
                        <div className="min-max">
                          <label className="container">
                            <input
                              type="radio"
                              className="quiz-radio"
                              name="answer"
                              value={3}
                              onChange={(e) => setAnswer(e.target.value)}
                              required
                            />
                            <FontAwesomeIcon className="paw" icon={faPaw} />
                          </label>
                        </div>
                        <div className="min-max">
                          <label className="container">
                            <input
                              type="radio"
                              className="quiz-radio"
                              name="answer"
                              value={4}
                              onChange={(e) => setAnswer(e.target.value)}
                              required
                            />
                            <FontAwesomeIcon className="paw" icon={faPaw} />
                          </label>
                        </div>
                        <div className="min-max">
                          <label className="container">
                            <input
                              type="radio"
                              className="quiz-radio"
                              name="answer"
                              value={5}
                              onChange={(e) => setAnswer(e.target.value)}
                              required
                            />
                            <FontAwesomeIcon className="paw" icon={faPaw} />
                          </label>
                        </div>
                      </div>
                    </div>
                  )}
                </div>
                <label>
                  Important?
                  <input
                    className="important-check"
                    type="checkbox"
                    id="important"
                    name="important"
                    value={isChecked}
                    onChange={checkBox}
                  />
                </label>
                <div className="submit-container">
                  <button
                    onClick={checkAnswer}
                    className="quiz-button"
                    type="submit"
                  >
                    Next{" "}
                    <FontAwesomeIcon className="arrow" icon={faRightLong} />
                  </button>
                </div>
              </div>
            </form>
          </div>
        </>
      )}
    </div>
  );
};

export default DisplayQuestion;
