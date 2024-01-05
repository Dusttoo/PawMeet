import { useState } from "react";
import { useHistory } from "react-router-dom";
import "./Search.css";

const SearchBar = () => {
  const history = useHistory();
  const [queryString, setQueryString] = useState(
    new URLSearchParams(history.location.search).get("q") ?? ""
  );
  const updateSearch = (e) => {
    setQueryString(e.target.value);
    if (e.target.value) {
      history.replace({
        pathname: history.location.pathname,
        search: `?q=${e.target.value}`,
      });
    } else {
      history.replace({
        pathname: "",
      });
    }
  };

  return (
    <div className="search-bar-container">
      <input
        className="search"
        placeholder="Search for a breed"
        type="search"
        value={queryString}
        onChange={updateSearch}
      />
    </div>
  );
};

export default SearchBar;
