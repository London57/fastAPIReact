import { createContext, useState, useEffect } from "react";

const UserContext = createContext();

function UserContextProvider({ children }) {
    const [userId, setUserId] = useState(null);
    const [userToken, setUserToken] = useState(null);

    // При загрузке компонента, пытаемся восстановить токен из localStorage
    useEffect(() => {
        const tokenFromStorage = localStorage.getItem('userToken');
        if (tokenFromStorage) {
            setUserToken(tokenFromStorage);
        }
    }, []);

    function logout() {
        setUserId(null);
        setUserToken(null);
        localStorage.removeItem('userToken'); // Очищаем токен из localStorage при выходе
    }

    // При изменении userToken сохраняем его в localStorage
    useEffect(() => {
        if (userToken) {
            localStorage.setItem('userToken', userToken);
        } else {
            localStorage.removeItem('userToken');
        }
    }, [userToken]);

    return (
        <UserContext.Provider value={{ userId, setUserId, logout, userToken, setUserToken }}>
            {children}
        </UserContext.Provider>
    );
}

export { UserContext, UserContextProvider };