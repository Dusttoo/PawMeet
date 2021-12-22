import React from "react";
import { Link } from "react-router-dom";
import { CircularProgressbarWithChildren } from "react-circular-progressbar";
import "./Percentage.css";
import "react-circular-progressbar/dist/styles.css";

const PercentageCircle = ({ percentage, image, breed }) => {
  return (
    <div className="progress-bar">
      <CircularProgressbarWithChildren
        styles={{
          root: {
            position: "relative",
          },
          path: {
            stroke: `rgba(138, 123, 78, ${percentage / 100})`,
            strokeLinecap: "round",
            transition: "stroke-dashoffset 0.5s ease 0s",
            transform: "rotate(0.25turn)",
            transformOrigin: "center center",
          },
          trail: {
            stroke: "#d6d6d6",
            strokeLinecap: "butt",
            transform: "rotate(0.25turn)",
            transformOrigin: "center center",
          },
          text: {
            fill: "#f88",
            fontSize: "16px",
          },
        }}
        value={percentage}
      >
        <div className="circle-contents">
          <h2 className="breed">
            <Link className="breed" to={`/breeds/${breed.id}`}>
              {breed.name}{" "}
            </Link>
          </h2>
          <Link className="image-link" to={`/breeds/${breed.id}`}>
            <img
              className="circle-image"
              src={image.img_url}
              alt={breed.name}
            />
          </Link>
          <div className="circle-result">
            <strong>{percentage}%</strong> match
          </div>
        </div>
      </CircularProgressbarWithChildren>
    </div>
  );
};

export default PercentageCircle;
