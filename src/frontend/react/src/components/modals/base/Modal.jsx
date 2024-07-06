
export default function Modal({body, classname}) {
    return (
        <dialog open className={classname}>{body}</dialog>
    )
}