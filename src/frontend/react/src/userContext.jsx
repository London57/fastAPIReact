import { createContext, useState } from "react";

const UserContext = createContext()

function UserContextProvider({children}) {
	const [userId, setUserId] = useState(null)

	function logout() {
		setUserId(null)
	}
	return (
		<UserContext.Provider value={{userId, setUserId, logout}}>
			{children}
		</UserContext.Provider>
	)
}

export { UserContext, UserContextProvider }
