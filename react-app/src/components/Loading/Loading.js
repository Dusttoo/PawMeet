import React from "react";
import GifPlayer from "react-gif-player";

const Loading = () => {
  return (
    <>
      <div className="loading-container">
        <GifPlayer gif="https://i.imgur.com/JS8bT2R.gif" autoplay={true} />
        <h2 className="highlighted-breed-name">Calling all the dogs...</h2>
      </div>
    </>
  );
};

export default Loading;
