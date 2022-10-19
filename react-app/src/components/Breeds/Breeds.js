import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { allBreedTraits } from "../../store/breed_traits";
import { allBreedAnswers } from "../../store/breed_answers";
import Loading from "../Loading/Loading";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSearch } from "@fortawesome/free-solid-svg-icons";
import SearchBar from "../Search/Search";
import SearchResults from "../Search/SearchResults";
import Pagination from "../Pagination";
import "./Breed.css";

const PAGE_SIZES = [15, 25, 50, 100];

const BreedsPage = () => {
  const breeds = useSelector((state) => state.breeds);
  const images = useSelector((state) => state.breed_images);
  const dispatch = useDispatch();
  const [loaded, setLoaded] = useState(false);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState(false);
  const [currentPage, setCurrentPage] = useState(1)
  const [pageSize, setPageSize] = useState(15)
  const currentPaginationData = Object.values(breeds)
  .sort(function (a, b) {
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
  .slice(pageSize * (currentPage - 1), pageSize * currentPage);
  console.log(currentPaginationData)
  const updateRowsPerPage = (pageSize) => {
    setPageSize(Number(pageSize))
    setCurrentPage(1)
  };
  const updatePage = (pageNumber) => {
    setCurrentPage(pageNumber)
    };

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

  const openSearch = () => {
    setSearch(!search);
  };

  return (
    <>
      {loading ? (
        <>
          <Loading />
        </>
      ) : (
        <div className="breed-list-container">
          <Pagination
            currentPage={currentPage}
            totalCount={Object.values(breeds).length}
            pageSize={pageSize}
            pageSizeOptions={PAGE_SIZES}
            onPageChange={updatePage}
            onPageSizeOptionChange={updateRowsPerPage}
          />
          <div className="header-search">
            <h2 className="breed-list-heading">Meet the Breeds</h2>
            <FontAwesomeIcon
              className="search-button"
              icon={faSearch}
              onClick={openSearch}
            />
          </div>
          {search ? (
            <>
              <div className="search-container">
                <SearchBar />
                {Object.values(breeds).map((item) => {
                  const findImage = Object.values(images).find(
                    (image) => image.breed_id === item.id
                  );
                  return <SearchResults breed={item} image={findImage} />;
                })}
              </div>{" "}
            </>
          ) : (
            <></>
          )}

          {currentPaginationData.map((breed) => {
              const thisImage = Object.values(images).find(
                (image) => image.breed_id === breed.id
              );
              if (thisImage) {
                return (
                  <div className="breed-list-item-container">
                    <img
                      className="breed-link-image"
                      src={thisImage.img_url}
                      alt={breed.name}
                    />
                    <Link className="breed" to={`/breeds/${breed.id}`}>
                      {breed.name}
                    </Link>
                  </div>
                );
              }
            })}
        </div>
      )}
    </>
  );
};

export default BreedsPage;
