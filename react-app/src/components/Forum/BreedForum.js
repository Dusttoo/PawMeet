import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { allPostsForGroup } from "../../store/group_posts";
import { useSelector } from "react-redux";
import { Link } from "react-router-dom";
import DisplayPosts from "./DisplayPost";
import { allUsers } from "../../store/users";
import { allComments } from "../../store/comments";
import ForumSidebar from "./SideBar";
import { useParams } from "react-router";
import Pagination from "../Pagination";
import "./Forum.css";

const PAGE_SIZES = [15, 25, 50, 100];

const BreedForum = () => {
  const dispatch = useDispatch();
  const { id } = useParams();
  const posts = useSelector((state) => state.group_posts);
  const breed_groups = useSelector((state) => state.groups);
  const [currentPage, setCurrentPage] = useState(1);
  const [pageSize, setPageSize] = useState(15);
  const sortedByTime = Object.values(posts).sort(function (a, b) {
    return new Date(b.posted) - new Date(a.posted);
  });
  const currentPaginationData = sortedByTime.slice(
    pageSize * (currentPage - 1),
    pageSize * currentPage
  );
  const updateRowsPerPage = (pageSize) => {
    setPageSize(Number(pageSize));
    setCurrentPage(1);
  };
  const updatePage = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  const headerImage = [
    "https://www.petfoodprocessing.net/ext/resources/PFP-Images/Articles-20/092920_Eukanuba-Premium-Performance_Lead.jpg?t=1601328222&width=1080",
    "https://imagesvc.meredithcorp.io/v3/mm/image?q=85&c=sc&rect=2%2C0%2C2000%2C1332&poi=face&w=2000&h=1333&url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2020%2F10%2F26%2Fbasset-hound-167768274-2000.jpg",
    "https://res.cloudinary.com/jacepharm/image/upload/v1548864318/Depositphotos_64511131_xl-2015-min_efkipp.jpg",
    "https://www.scruffylittleterrier.com/wp-content/uploads/2020/07/AdobeStock_336595006-2880x1800.jpeg",
    "https://blogstudio.s3.amazonaws.com/sitstay/3963c6cbd12033c4a966c0c9a62c9c05.jpg",
    "https://www.nativebreed.org/wp-content/uploads/2020/06/Bulldog.jpg",
    "https://thehappypuppysite.com/wp-content/uploads/2018/01/herding.jpg",
  ];

  useEffect(() => {
    dispatch(allPostsForGroup(id));
    dispatch(allUsers());
    dispatch(allComments());
  }, [dispatch, id]);

  return (
    <>
      <div className="page-container">
        <ForumSidebar />
        <div className="forum-container">
          <div
            className="forum-header-image"
            style={{ backgroundImage: `url(${headerImage[id - 1]})` }}
          >
            <h1 className="forum-header">{breed_groups[id].name}</h1>
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

            {currentPaginationData.map((post) => {
              return <DisplayPosts post={post} />;
            })}
          </table>
          {Object.keys(posts).length ? <></> : <h2>No Posts Yet!</h2>}
          <Pagination
            currentPage={currentPage}
            totalCount={sortedByTime.length}
            pageSize={pageSize}
            pageSizeOptions={PAGE_SIZES}
            onPageChange={updatePage}
            onPageSizeOptionChange={updateRowsPerPage}
          />
        </div>
      </div>
    </>
  );
};

export default BreedForum;
