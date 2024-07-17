import Form from '../base/Form.jsx'

export default function RegistrationForm() {
	return (
		<Form classname='form' fields={['email', 'username', 'password']} url_to_send_form={'http://localhost:8080/auth/register'} />
	)
}