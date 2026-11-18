import { useEffect, useState } from 'react'
import './App.css'

function App() {

  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    fetch("http://localhost:8000/")
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch(() => setMessage("Could not reach backend"));
  }, []);
  
  return <h1>{message}</h1>;
}

export default App
