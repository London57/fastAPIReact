import RegistrationForm from './components/forms/RegistrationForm/RegistrationForm.jsx'

import Menu from './components/menu/Menu.jsx'

import { useState } from 'react'

export default function App() {
  const [menuState, setMenuState] = useState('Tasks')
  return (
   <>
   <Menu active={menuState} changeF={(currentActive) => setMenuState(currentActive)} />
   {menuState === 'Tasks' && (
    <p>Tasks</p>
   )}
   {menuState === 'Registration' && (
     <RegistrationForm />
   )}
  </> 
  )
}