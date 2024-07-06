export default function Button({onclick, text, classname}) {
    return (
        <button className={classname} onClick={onclick}>{text}</button>
    )
}