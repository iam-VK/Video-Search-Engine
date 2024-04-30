import React from 'react';

const VideoPlayer = ({ videoPath }) => {
  return (
    <div>
      <br /><br /><br />
      <video controls>
        <source src={videoPath} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>
  );
};

export default VideoPlayer;
