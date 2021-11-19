import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link, useParams } from 'react-router-dom';
import { allPets, removePet } from '../../store/pets';
import { useHistory } from 'react-router';
import { Carousel } from 'react-carousel-minimal';
import './Breed.css'
import { faBorderNone } from '@fortawesome/free-solid-svg-icons';
import { allBreedAnswers } from '../../store/breed_answers';
import { allBreedTraits } from '../../store/breed_traits';



const BreedInfo = () => {
    const {id} = useParams()
    const dispatch = useDispatch()
    const breeds = useSelector(state => state.breeds)
    const images = useSelector(state => state.breed_images)
    const breedTraits = useSelector(state => state.breed_traits)
    const breedAnswers = useSelector(state => state.breed_answers)
    const [loaded, setLoaded] = useState(false);
    // let thisAnswer = ''
    const theseAnswers = []
    Object.values(breedAnswers).map((answer) => {
      if(+answer.breed_id === +id) {
        theseAnswers.push(answer)
      }
    })


    useEffect(() => {
    (async() => {
      await dispatch(allBreedTraits())
      await dispatch(allBreedAnswers())
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

    const data = []
    Object.values(images).map((image) => {
        if(+image.breed_id === +id) {
            data.push({
            'image': image.img_url,
            'caption': breeds[id].name})
        }
    })


  const captionStyle = {
    fontSize: '2em',
    fontWeight: 'bold',
  }


  const traits =  breeds[id].personality.split(',')
  const personality = []
  console.log(traits)
  traits.map(word => {
      if(word.includes('{')) {
          console.log('{ true')
        personality.push(word.replace('{', ''))
      } else if(word.includes('}')) {
        personality.push(word.replace('}', ''))
      } else {
          personality.push(word)
      }
  })

  console.log(personality)



    return (
        <>
          <div className='breed-container'>
            <div className='carousel-container'>
                <Carousel
                className='carousel'
                data={data}
                time={6000}
                width="850px"
                height="500px"
                captionStyle={captionStyle}
                radius="10px"
                slideNumber={false}
                // slideNumberStyle={slideNumberStyle}
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
            <div className='breed-content'>
                <h2>{personality[0]} {personality[1]} {personality[2]}</h2>
                <p>{breeds[id].description}</p>
            </div>
            <div className='breed-traits-container'>
              {Object.values(breedTraits).map((trait) => {
                const thisAnswer = theseAnswers.find((answer) => +answer.trait_id === +trait.id)
                return (
                <>
                  <h2 className='trait-header'>{trait.trait}</h2>
                  <p className='trait-description'>{trait.description}</p>
                  <div className="star-rating">
                  {thisAnswer.trait_id === 7 || thisAnswer.trait_id === 8 ?
                  <></> :
                  [...Array(5)].map((star, rate) => {
                  rate += 1;
                  return (

                    <button
                      type="button"
                      key={rate}
                      className={rate <= thisAnswer.answer ? "on" : "off"}
                    >
                      <span className="bubble"></span>
                    </button>
                  );
                })}
                  {thisAnswer.trait_id === 8 ?
                  [...Array(3)].map((star, rate) => {
                  rate += 1;
                  const coatLengths = ['', 'Short', 'Medium', 'Long']
                  return (

                    <button
                      type="button"
                      key={rate}
                      className={rate === thisAnswer.answer ? "on" : "off"}
                    >
                      <span className="bubble">{coatLengths[rate]}</span>
                    </button>
                  );
                }) : null}
                  {thisAnswer.trait_id === 7 ? 
                  [...Array(9)].map((star, rate) => {
                  rate += 1;
                  const coatTypes = ['', 'Wiry', 'Rough', 'Curly', 'Hairless', 'Corded', 'Wavy', 'Smooth', 'Double', 'Silky']
                  return (

                    <button
                      type="button"
                      key={rate}
                      className={rate === thisAnswer.answer ? "on" : "off"}
                    >
                      <span className="bubble">{coatTypes[rate]}</span>
                    </button>
                  );
                }) : <></>}

                
                
              </div>
                </>
                
                )
              })}
            </div>
          </div>

        </>
    )
}

export default BreedInfo