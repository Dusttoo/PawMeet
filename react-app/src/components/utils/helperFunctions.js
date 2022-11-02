// -- Post Like Helpers ------------------------------
export const getLikes = (likes, postId) => {
  let numLikes = 0;
  likes.map((like) => {
    if (like.post_id === +postId) {
      numLikes++;
    }
  });
  return numLikes;
};

export const sortedByTime = (list) => {
  list.sort(function (a, b) {
    return new Date(a.posted) - new Date(b.posted);
  });
  return list;
};

// -- Breed Helpers ------------------------------

export const cleanUpTraits = (traits) => {
  const personality = [];
  traits.split(",").map((word) => {
    if (word.includes("{")) {
      personality.push(word.replace("{", ""));
    } else if (word.includes("}")) {
      personality.push(word.replace("}", ""));
    } else {
      personality.push(word);
    }
  });

  return personality;
};

export const sortBreedsByName = (list) => {
  list.sort(function (a, b) {
    let nameA = a.name.toUpperCase();
    let nameB = b.name.toUpperCase();
    if (nameA < nameB) {
      return -1;
    }
    if (nameA > nameB) {
      return 1;
    }
    return 0;
  });
  return list;
};

export const getTenBreeds = (breeds) => {
  const tenBreeds = [];
  const breedId = [];
  for (let i = 0; i < 11; i++) {
    const add =
      breeds[getRandomInt(1, Object.keys(breeds).length - 1)];
    if (!breedId.includes(add.id)) {
      tenBreeds.push(add);
      breedId.push(add.id);
    }
  }
  return tenBreeds;
};

export const getRandomImage = (min, breedImages) => {
  const max = breedImages.length
  const num = Math.floor(Math.random() * (max - min) + min);
  const image = breedImages[num];
  return image.img_url
};

export const calculateResults = (breeds, breedAnswers, userAnswers) => {
  const results = [];

  Object.values(breeds).map((breed) => {
    let total = 0;
    let average = 0;
    const breedResponses = Object.values(breedAnswers).filter(
      (answer) => +answer.breed_id === +breed.id
    );
    const userResponses = Object.values(userAnswers);
    for (let i = 0; i < breedResponses.length; i++) {
      if (userResponses[i].important === true) {
        if (breedResponses[i].answer === userResponses[i].answer) {
          total += 2;
        } else total--;
      } else {
        if (breedResponses[i].answer === userResponses[i].answer) {
          total++;
        }
      }
    }

    average = (total / breedResponses.length) * 100;
    results.push([breed.id, average]);
  });
  results.sort(function (a, b) {
    return b[1] - a[1];
  });
  return results
};

// -- utility functions --------------------------------
export const getRandomInt =(min, max) => {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min); //The maximum is exclusive and the minimum is inclusive
}

export const getFivePosts = (posts) => {
  return sortedByTime(posts).splice(0, 5);
};

export const modifyTime = (time) => {
  const date = time.replace("00:00:00 GMT", "");
  return date;
};
