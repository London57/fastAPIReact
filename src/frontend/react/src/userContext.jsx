import { createContext, useState } from "react";

const UserContext = createContext()

function UserContextProvider({children}) {
	const [userId, setUserId] = useState(null)
	const [userToken, setUserToken] = useState(null)

	function logout() {
		setUserId(null)
	}
	return (
		<UserContext.Provider value={{userId, setUserId, logout, userToken, setUserToken}}>
			{children}
		</UserContext.Provider>
	)
}

export { UserContext, UserContextProvider }
