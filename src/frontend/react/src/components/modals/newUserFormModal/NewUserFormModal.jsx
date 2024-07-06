import Modal from "../base/Modal";
import NewUserForm from "../../forms/NewUserForm";

import './NewUserFormModal.css'

export default function NewUserFormModal() {
    return (
        <Modal body={<NewUserForm />} classname='dialog' />
    )
}