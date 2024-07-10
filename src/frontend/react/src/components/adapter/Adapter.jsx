import Button from '../buttons/base/Button.jsx'


export default function Adapter({active, changeF}) {
    return (
        <section>
            <Button isActive={active === 'Userlist'} onClick={() => changeF('Userlist')} className="adaptButton">
                User list
            </Button>
            <Button isActive={active === 'Registration'} onClick={() => changeF('Registration')} className="adaptButton">
                Registration
            </Button>
        </section>
    )
}