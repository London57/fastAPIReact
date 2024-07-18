import Button from '../buttons/base/Button.jsx'


export default function Menu({active, changeF}) {
    return (
        <section>
            <Button classname={active === 'Tasks' ? 'button active' : 'button'} onclick={() => changeF('Tasks')} text='Tasks' />
            <Button classname={active === 'Registration' ? 'button active' : 'button'} onclick={() => changeF('Registration')}text='Registration' />
        </section>
    )
}