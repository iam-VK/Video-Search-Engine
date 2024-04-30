import React, { useState, useEffect } from 'react';
import axios from 'axios';
import VideoPlayer from '../videoplayer/VideoPlayer';

const SearchResult = ({ inputValue }) => {
  const [searchResults, setSearchResults] = useState(null);
  const [error, setError] = useState(null);
  const [showVideo, setShowVideo] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      try {
        if (inputValue) {
          const response = await axios.get(`http://localhost:5000/search/${inputValue}`);
          setSearchResults(response.data);
          setError(null);
          setShowVideo(false); // Hide video initially
        } else {
          // Clear search results and error when input value is empty
          setSearchResults(null);
          setError(null);
        }
      } catch (error) {
        setSearchResults(null);
        setError(error.message);
      }
    };

    fetchData();
  }, [inputValue]);

  const handleGetVideo = () => {
    setShowVideo(true); // Show video when Get Video button is clicked
  };

  return (
    <div>
      {error && <div>Error: {error}</div>}
      
      {searchResults && (
        <div>
          <h2>Search Results:</h2>
          <p>File Name: {searchResults.file_name}</p>
          <p>Category List: {searchResults.category_list}</p>
          <p>File Path: {searchResults.file_path}</p>
          <button onClick={handleGetVideo}>Get Video</button>
        </div>
      )}

      {showVideo && searchResults && <VideoPlayer videoPath={searchResults.file_path} />}
    </div>
  );
};

export default SearchResult;
