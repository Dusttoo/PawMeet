import { useLocation, Link } from "react-router-dom";

const SearchResults = ({ breed, image }) => {
  const queryString = new URLSearchParams(useLocation().search).get("q") ?? "";
  const breedName = breed.name;
  const lowerString = queryString.toLowerCase();

  return (
    <>
      {!queryString ? (
        <div className="search-results-empty"></div>
      ) : (
        breedName.toLowerCase().includes(lowerString) && (
          <div className="result-container">
            <div className="search-results">
              <div className="breed-list-item-container">
                {image && (
                  <img
                    className="breed-link-image"
                    src={image.img_url}
                    alt={breed.name}
                  />
                )}
                <Link className="breed" to={`/breeds/${breed.id}`}>
                  {breed.name}
                </Link>
              </div>
            </div>
          </div>
        )
      )}
    </>
  );
};

export default SearchResults;
