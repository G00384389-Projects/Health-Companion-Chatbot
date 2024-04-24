import React, { useState, useEffect } from 'react';
import axios from 'axios';

// The NewsList component fetches and displays a list of news articles
const NewsList = () => {
  // State variable for storing articles
  const [articles, setArticles] = useState([]);
  // State variable for storing any error during the fetch
  const [error, setError] = useState('');

  // useEffect to fetch news articles when the component mounts
  useEffect(() => {
    // Async function to fetch data
    const fetchData = async () => {
      // The base URL for the NewsAPI
      const API_URL = 'https://newsapi.org/v2/everything';
      // API key 
      const API_KEY = '13f23cf681c84f41848b57dda93a6694'; 
      // Query parameters for the API call
      const queryParams = {
        q: 'Apple', // Query term
        from: '2024-04-23', // Start date for the news articles
        sortBy: 'popularity', // Sorting parameter
        apiKey: API_KEY // API key parameter
      };

      try {
        // Perform the API request with axios
        const response = await axios.get(API_URL, { params: queryParams });
        console.log(response); // Log the response to the console for debugging
        setArticles(response.data.articles); // Update the articles state with the fetched data
      } catch (error) {
        console.error('Error fetching news:', error); 
        setError('Failed to fetch news'); 
      }
    };

    fetchData(); // Call the fetch data 
  }, []); 

  // Conditionally render an error message if there's an error
  if (error) {
    return <div>Error: {error}</div>;
  }

  // Render the list of articles
  return (
    <div className="news-container">
      <h1>World News</h1> 
      {articles.map((article, index) => (
        // Map over the articles array to render each article
        <div key={index} className="news-article">
          <h2>{article.title}</h2> 
          <p>{article.author}</p> 
          <p>{article.description}</p> 
          {/* Render the article image if the URL is available */}
          {article.urlToImage && <img src={article.urlToImage} alt={article.title} />}
          {/* link to read the full article */}
          <p><a href={article.url} target="_blank" rel="noopener noreferrer">Read more</a></p>
        </div>
      ))}
    </div>
  );
};

export default NewsList;
