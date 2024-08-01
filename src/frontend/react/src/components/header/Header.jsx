import './Header.css'
import { Outlet, NavLink } from 'react-router-dom'

import ProfileButton from '../buttons/profileButton/ProfileButton'

export default function Header() {
    return (
        <>
            <section className='headerSection'>
                <header className='header'>
                    <NavLink className='link' to='/' style={{marginRight: '5px'}}>button</NavLink>
                </header>
                <NavLink to='profile'>
                <ProfileButton /></NavLink>
            </section>
            <Outlet /> 
        </>
    )
}
