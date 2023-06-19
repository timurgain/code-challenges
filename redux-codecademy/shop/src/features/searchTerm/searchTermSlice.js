export const setSearchTerm = (query) => {
  return {
    type: "searchTerm/setSearchTerm",
    payload: query,
  };
};

export const clearSearchTerm = () => {
  return {
    type: "searchTerm/clearSearchTerm",
  }
};

const initialSearchTerm = "";
export const searchTermReducer = (search = initialSearchTerm, action) => {
  switch (action.type) {
    case "searchTerm/setSearchTerm":
      return action.payload;
    case "searchTerm/clearSearchTerm":
      return "";
    default:
      return search;
  }
};
