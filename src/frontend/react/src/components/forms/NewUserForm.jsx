import Form from "./base/Form";

export default function NewUserForm() {
    return (
        <Form fields={['name']} url_to_send_form={'http://localhost:8080/users'}/>
    )
}