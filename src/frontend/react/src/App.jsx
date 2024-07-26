import {BrowserRouter, Routes, Route, Link} from 'react-router-dom'

import Header from './components/header/Header.jsx'
import RegistrationForm from './components/forms/RegistrationForm/RegistrationForm.jsx'

import ProfilePage from './components/profilePage/ProfilePage.jsx'


import '../src/App.css' 


export default function App() {
  
  return (
  <BrowserRouter>
   <Routes>
    <Route path='/' element={<Header />} >
      <Route index element={<h1>Welcome!</h1>} />
    </Route>
    <Route path='/registration' element={<RegistrationForm />} />
    <Route path='profile' element={<ProfilePage />} />
   </Routes>
  </BrowserRouter>
  )
}