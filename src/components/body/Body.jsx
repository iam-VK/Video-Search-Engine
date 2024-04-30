import { TextareaAutosize as BaseTextareaAutosize } from '@mui/base/TextareaAutosize';
import { styled } from '@mui/system';
import "./body.css"
import SearchResult from '../search_result/SearchResult.jsx';
import React from 'react';

function Body({ path })
{
  const [inputValue, setInputValue] = React.useState('');
  const handleInputChange = (event) =>
  {
    setInputValue(event.target.value);
  };

  return (
    <>
    <br />
    <br />
    <br />
    <br />
      <div className='textbox'>
        <TextareaAutosize
          aria-label="empty textarea"
          placeholder="Search Query"
          onChange={handleInputChange}
          value={inputValue}
        />
      </div>
      <br />
      <SearchResult inputValue={inputValue} path={path} />
    </>
  )
}



const blue = {
  100: '#DAECFF',
  200: '#b6daff',
  400: '#3399FF',
  500: '#007FFF',
  600: '#0072E5',
  900: '#003A75',
};

const grey = {
  50: '#f6f8fa',
  100: '#eaeef2',
  200: '#d0d7de',
  300: '#afb8c1',
  400: '#8c959f',
  500: '#6e7781',
  600: '#57606a',
  700: '#424a53',
  800: '#32383f',
  900: '#24292f',
};

const TextareaAutosize = styled(BaseTextareaAutosize)(
  ({ theme }) => `
  width: 320px;
  font-family: IBM Plex Sans, sans-serif;
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5;
  padding: 12px;
  border-radius: 12px 12px 0 12px;
  color: ${theme.palette.mode === 'dark' ? grey[300] : "#F9F6EE"};
  background: ${theme.palette.mode === 'dark' ? grey[900] : '#010203'};
  border: 1px solid ${theme.palette.mode === 'dark' ? grey[700] : grey[200]};
  box-shadow: 0px 2px 24px ${theme.palette.mode === 'dark' ? "#010203" : "#010203"};
  transition: box-shadow 0.2s;

  &:hover {
    border-color: #ffa500};
  }

  &:focus {
    color: ${"#ffffff"};
    border-color: ${"#010203"};
    box-shadow: 0px 2px 24px ${theme.palette.mode === 'dark' ? "#ffff" : "#ffff"};
  }
  }
`,
);

export default Body