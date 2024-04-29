import {Route, BrowserRouter as Router, Routes } from 'react-router-dom'
import './App.css'
import Home from './pages/Home'
import Contact from './pages/Contact'

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path='/app/home' element={<Home />}/>
          <Route path='/app/contact' element={<Contact />}/>
        </Routes>
      </Router>
    </>
  )
}

export default App
