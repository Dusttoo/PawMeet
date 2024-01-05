export const DOTS = "...";

function usePagination({ currentPage, totalCount, pageSize }) {
  const totalPages = Math.ceil(totalCount / pageSize);
  if (totalPages === 1) {
    return [1];
  }
  if (currentPage === 1 || currentPage === 2) {
    return [1, 2, 3, DOTS, totalPages];
  } else if (currentPage > 1 && currentPage < totalPages - 1) {
    return [
      1,
      DOTS,
      currentPage - 1,
      currentPage,
      currentPage + 1,
      DOTS,
      totalPages,
    ];
  } else if (currentPage + 1 === totalPages) {
    return [1, DOTS, currentPage - 1, currentPage, totalPages];
  } else {
    return [1, DOTS, currentPage - 1, currentPage];
  }
}

export default usePagination;
