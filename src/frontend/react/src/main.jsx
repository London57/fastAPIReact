import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import Provider from './provider.jsx'
import {UserContextProvider} from './userContext.jsx'


ReactDOM.createRoot(document.getElementById('root')).render(
    <UserContextProvider>
        <Provider>
            <App />
        </Provider>
    </UserContextProvider>
)
   



// ReactDOM.createRoot(document.getElementById('root')).render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
// )