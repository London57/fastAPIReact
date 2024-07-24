import '../header/Header.css'
import { Outlet, NavLink } from 'react-router-dom'

export default function Header() {
    return (
        <>
            <header className='header'>
                <NavLink className='link' to='/' style={{marginRight: '5px'}}>home</NavLink>
                <NavLink className='link' to='/registration'>registration</NavLink>
            </header>
            <Outlet />
        </>
    )
}