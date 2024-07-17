import '../base/Button.css'


export default function Button({onclick, text, isActive}) {
    return (
        <button className='button' onClick={onclick}>{text}</button>
    )
}