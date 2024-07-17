import Button from '../buttons/base/Button.jsx'


export default function Menu({active, changeF}) {
    return (
        <section>
            <Button isActive={active === 'Userlist'} onclick={() => changeF('Tasks')} text='Tasks' />
            <Button isActive={active === 'Registration'} onclick={() => changeF('Registration')}text='Registration' />
        </section>
    )
}