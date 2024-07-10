
import Button from './components/buttons/base/Button.jsx'
import UserList from './components/userList/UserList.jsx'
import { useMemo } from 'react'

import { useState} from 'react'

import NewUserFormModal from './components/modals/newUserFormModal/NewUserFormModal.jsx'
import Form from './components/forms/base/Form.jsx'

export default function App() {
  const [page, setPage] = useState('userList')
  // const memoUserList = useMemo(() => (
  //   <UserList />
  // ), [])

  function handleClick(text) {
    setContent(text)
  }
  

  return (
   <>
      <NewUserFormModal />
     <UserList />
      {/* {memoUserList} */}
      <Form fields={['name', 'last name']} />
  </> 
  )
}