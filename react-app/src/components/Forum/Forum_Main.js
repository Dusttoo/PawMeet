import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { allPosts } from "../../store/forum";
import { useSelector } from "react-redux";
import { Link } from "react-router-dom";
import "./Forum.css";
import DisplayPosts from "./DisplayPost";
import { allUsers } from "../../store/users";
import { allComments } from "../../store/comments";
import ForumSidebar from "./SideBar";
import MainNext from "./MainNext";
import MainPrevious from "./MainPrevious";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faAngleLeft, faAngleRight } from "@fortawesome/free-solid-svg-icons";

const ForumHome = () => {
  const dispatch = useDispatch();
  const posts = useSelector((state) => state.forum);
  const [index, setIndex] = useState(0);
  const remove = 10;
  const [next, setNext] = useState(false);
  const [first, setFirst] = useState(true);
  const [previous, setPrevious] = useState(false);
  const [pageNum, setPageNum] = useState(1);

  useEffect(() => {
    dispatch(allPosts());
    dispatch(allUsers());
    dispatch(allComments());
  }, [dispatch]);

  const sortedByTime = Object.values(posts).sort(function (a, b) {
    return new Date(b.posted) - new Date(a.posted);
  });

  const getTenPosts = () => {
    return sortedByTime.splice(index, remove);
  };

  const showNext = () => {
    const lastPage = Math.ceil(sortedByTime.length / 10);
    if (lastPage === pageNum) {
      return null;
    } else {
      setFirst(false);
      setNext(true);
      setPageNum(pageNum + 1);
      if (sortedByTime.length - index < 10) {
        setIndex(index + (sortedByTime.length - index));
      } else {
        setIndex(index + 10);
      }
    }
  };

  const showPrevious = () => {
    if (pageNum < 2) {
      setFirst(true);
      setPrevious(false);
    } else {
      setPageNum(pageNum - 1);
      setFirst(false);
      setNext(false);
      setPrevious(true);
      setIndex(index - 10);
    }
  };

  return (
    <>
      <div className="page-container">
        <ForumSidebar />
        <div className="forum-container">
          <div
            className="forum-header-image"
            style={{
              backgroundImage:
                "url('https://penntoday.upenn.edu/sites/default/files/2019-10/iStock-1094310798.jpg')",
            }}
          >
            <h1 className="forum-header">Speak!</h1>
          </div>
          <div className="forum-options">
            <Link to="/forum/add" className="add-post">
              Add Post
            </Link>
          </div>
          <table className="forum-table">
            <tr>
              <th style={{ width: "10%" }} className="table-label">
                Author
              </th>
              <th style={{ width: "65%" }} className="table-label">
                Title
              </th>
              <th style={{ width: "23%" }} className="table-label">
                Date
              </th>
              <th style={{ width: "2%" }} className="table-label">
                Comments
              </th>
            </tr>
            {first ? (
              getTenPosts().map((post) => {
                return <DisplayPosts post={post} />;
              })
            ) : (
              <></>
            )}
            {next ? <MainNext index={index} posts={sortedByTime} /> : <></>}
            {previous ? (
              <MainPrevious index={index} allPosts={sortedByTime} />
            ) : (
              <></>
            )}
          </table>
          <div className="next-prev-container">
            <FontAwesomeIcon
              icon={faAngleLeft}
              className="next-prev"
              onClick={showPrevious}
            />
            <FontAwesomeIcon
              icon={faAngleRight}
              className="next-prev"
              onClick={showNext}
            />
          </div>
          <div className="page-num-container">
            <p>{pageNum}</p>
          </div>
        </div>
      </div>
    </>
  );
};

export default ForumHome;
