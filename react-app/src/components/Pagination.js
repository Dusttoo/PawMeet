import usePagination, { DOTS } from "../components/utils/pagination";
import React from "react";
import PropTypes from "prop-types";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faChevronRight,
  faChevronLeft,
} from "@fortawesome/free-solid-svg-icons";
import "./pagination.css";

function Pagination({
  onPageChange,
  onPageSizeOptionChange,
  totalCount,
  currentPage,
  pageSize,
  pageSizeOptions,
}) {
  const paginationRange = usePagination({
    currentPage,
    totalCount,
    pageSize,
  });

  const onNext = () => {
    onPageChange(currentPage + 1);
  };

  const onPrevious = () => {
    onPageChange(currentPage - 1);
  };

  return (
    <ul className="wrapper">
      <li className="paginationItem">
        <button
          type="button"
          className="arrowButton left"
          onClick={onPrevious}
          disabled={currentPage === 1 ? true : false} // change this line to disable a button.
        >
          <FontAwesomeIcon className="search-button" icon={faChevronLeft} />
        </button>
      </li>

      {paginationRange.map((pageNumber) => {
        if (pageNumber === DOTS) {
          return <li className="dots">&#8230;</li>;
        }
        return (
          <li
            className="paginationItem"
            aria-current={pageNumber === currentPage && "page"} // change this line to highlight a current page.
          >
            <button type="button" onClick={() => onPageChange(pageNumber)}>
              {pageNumber}
            </button>
          </li>
        );
      })}

      <li className="paginationItem">
        <button
          type="button"
          className="arrowButton right"
          aria-label="Goto next page"
          onClick={onNext}
          disabled={
            Math.ceil(totalCount / pageSize) === currentPage ? true : false
          } // change this line to disable a button.
        >
          <FontAwesomeIcon className="search-button" icon={faChevronRight} />
        </button>
      </li>

      <select
        className="paginationSelector"
        value={pageSize}
        onChange={(e) => {
          onPageSizeOptionChange(e.target.value);
        }}
      >
        {pageSizeOptions.map((size) => (
          <option key={size} defaultValue={pageSize === size} value={size}>
            {size} per page
          </option>
        ))}
      </select>
    </ul>
  );
}

Pagination.propTypes = {
  totalCount: PropTypes.number,
  currentPage: PropTypes.number,
  pageSize: PropTypes.number,
  pageSizeOptions: PropTypes.instanceOf(Array),
  onPageChange: PropTypes.func,
  onPageSizeOptionChange: PropTypes.func,
};

Pagination.defaultProps = {
  totalCount: 0,
  currentPage: 1,
  pageSize: 1,
  pageSizeOptions: [15, 25, 50, 100],
  onPageChange: () => {},
  onPageSizeOptionChange: () => {},
};

export default Pagination;
