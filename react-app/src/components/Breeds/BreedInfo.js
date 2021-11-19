import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';
import { Link, useParams } from 'react-router-dom';
import { allPets, removePet } from '../../store/pets';
import { useHistory } from 'react-router';
import { Carousel } from 'react-carousel-minimal';
import './Breed.css'
import { faBorderNone } from '@fortawesome/free-solid-svg-icons';



const BreedInfo = () => {
    const {id} = useParams()
    const breeds = useSelector(state => state.breeds)
    const images = useSelector(state => state.breed_images)
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
          </div>

        </>
    )
}

export default BreedInfo