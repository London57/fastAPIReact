
import Button from './components/buttons/base/Button.jsx'
import UserList from './components/userList/UserList.jsx'
import { useMemo } from 'react'

import { useState} from 'react'

import NewUserFormModal from './components/modals/newUserFormModal/NewUserFormModal.jsx'
import Form from './components/forms/base/Form.jsx'

export default function App() {
  const [content, setContent] = useState("Click on button")

  const memoUserList = useMemo(() => (
    <UserList />
  ), [])

  function handleClick(text) {
    setContent(text)
  }
  
  return (
   <>
      <NewUserFormModal />
      {memoUserList}
      
      <Button text="first" onclick={() => handleClick('first')}/>
      <Button text="second" onclick={() => handleClick('second')} />
      <p>{content}</p>
      <Form fields={['name', 'last name']} />
  </> 
  )
}