import './App.css';
import {GetNews} from './api'
import React from "react";
import { useState, useEffect } from 'react';

function News_one({props}) {
  return (
    <div className='News_one'>
      <li>
        <h2>{props.title}</h2>
        <h4>{props.link}</h4>
        author: {props.author}, rating: {props.rate}
      </li>
    </div>
  )
}


function App() {
  const [news, SetNews] = useState([]);
  
  useEffect(() => {
    GetNews(100).then(data => {
    SetNews(data)
  }
)}, []);

  const NewsItems = news.map(el => <News_one props = {el}/>);
  return (
    <div className="App">
      <h1>HACKER NEWS</h1>
      <ol>
        {NewsItems}
      </ol>
    </div>
  );
};

export default App;
