import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { Carousel } from "react-carousel-minimal";
import { allBreedAnswers } from "../../store/breed_answers";
import { allBreedTraits } from "../../store/breed_traits";
import DisplayTraits from "./DisplayTraits";
import Loading from "../Loading/Loading";
import { cleanUpTraits } from "../utils/helperFunctions";
import "./Breed.css";

const BreedInfo = () => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const breeds = useSelector((state) => state.breeds);
  const images = useSelector((state) => state.breed_images);
  const breedTraits = useSelector((state) => state.breed_traits);
  const breedAnswers = useSelector((state) => state.breed_answers);
  const breedGroups = useSelector((state) => state.groups);
  const group = Object.values(breedGroups).find(
    (thisGroup) => +thisGroup.id === +breeds[id].breed_group
  );
  const [loaded, setLoaded] = useState(false);
  const [loading, setLoading] = useState(true);
  const personality = cleanUpTraits(breeds[id].personality)

  const theseAnswers = Object.values(breedAnswers).filter((answer) => +answer.breed_id === +id);

  useEffect(() => {
    (async () => {
      await dispatch(allBreedTraits());
      await dispatch(allBreedAnswers());
      setLoaded(true);
      setLoading(false);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  const data = [];
  Object.values(images).map((image) => {
    if (+image.breed_id === +id) {
      data.push({
        image: image.img_url,
        caption: breeds[id].name,
      });
    }
  });

  const captionStyle = {
    fontSize: "2em",
    fontWeight: "bold",
  };

  return (
    <>
      {loading ? (
        <>
          <Loading />
        </>
      ) : (
        <div className="breed-container">
          <div className="carousel-container">
            <Carousel
              className="carousel"
              data={data}
              time={6000}
              width="850px"
              height="500px"
              captionStyle={captionStyle}
              radius="10px"
              slideNumber={false}
              captionPosition="bottom"
              automatic={true}
              dots={true}
              pauseIconColor="white"
              pauseIconSize="40px"
              slideBackgroundColor="darkgrey"
              slideImageFit="cover"
              thumbnails={true}
              thumbnailWidth="100px"
              style={{
                textAlign: "center",
                maxWidth: "850px",
                maxHeight: "500px",
                margin: "40px auto",
              }}
            />
          </div>
          <div className="breed-content">
            <h2>The {breeds[id].name} is in the:</h2>
            <h3>{group.name} group</h3>
            <p>{group.description}</p>
            <h2>The {breeds[id].name} is:</h2>
            <h3>
              {personality[0]} - {personality[1]} - {personality[2]}
            </h3>
            <p className="breed-description">{breeds[id].description}</p>
            <div className="breed-details">
              <div className="breed-info-container">
                <h3 className="breed-info-header">Life Expectancy</h3>
                <p className="breed-description">{breeds[id].avg_life_exp}</p>
              </div>
              <div className="breed-info-container">
                <h3 className="breed-info-header">Average Height</h3>

                <p className="breed-description">
                  Males: {breeds[id].avg_height.males}
                </p>
                <p className="breed-description">
                  Females: {breeds[id].avg_height.females}
                </p>
              </div>

              <div className="breed-info-container">
                <h3 className="breed-info-header">Average Weight</h3>

                <p className="breed-description">
                  Males: {breeds[id].avg_weight.males}
                </p>
                <p className="breed-description">
                  Females: {breeds[id].avg_height.females}
                </p>
              </div>
            </div>
          </div>
          <div className="breed-traits-container">
            {Object.values(breedTraits).map((trait) => {
              const thisAnswer = theseAnswers.find(
                (answer) => +answer.trait_id === +trait.id
              );
              return <DisplayTraits trait={trait} thisAnswer={thisAnswer} />;
            })}
          </div>
        </div>
      )}
    </>
  );
};

export default BreedInfo;
