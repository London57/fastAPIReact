import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import Provider from './provider.jsx'


ReactDOM.createRoot(document.getElementById('root')).render(
    <Provider>
    <App />
    </Provider>
)
   



// ReactDOM.createRoot(document.getElementById('root')).render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
// )