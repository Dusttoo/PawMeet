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
    console.log(list)
    list.sort(function (a, b) {
    return new Date(a.posted) - new Date(b.posted);
  })
  return list
};

// -- Breed Helpers ------------------------------

export const cleanUpTraits = (traits) => {
  const personality = [];
  traits.split(",").map((word) => {
    console.log(word)
    if (word.includes("{")) {
      personality.push(word.replace("{", ""));
    } else if (word.includes("}")) {
      personality.push(word.replace("}", ""));
    } else {
      personality.push(word);
    }
  });

  return personality
}

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
  })
  return list
}


