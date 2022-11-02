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

