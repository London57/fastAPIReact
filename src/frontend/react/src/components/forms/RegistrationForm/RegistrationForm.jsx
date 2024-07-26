import '../base/Form.css'
import './RegistrationForm.css'
import SchemeHostPortOfURL from '../../../baseSchemeHostPortOfURL.js'

import { UserContext } from '../../../userContext.jsx'

import { useContext, useState, useEffect } from 'react'
import axios from "axios"

import { useNavigate } from 'react-router-dom'

export default function RegistrationForm() {
	let fields = ['email', 'username', 'password', 'repeat_password'];
	let formFields = fields.map((value, index) => (
			<div className="formElement" key={index}>
					<input type="text" name={value} style={{ marginBottom: '2em', marginLeft: '2px' }} placeholder={value} />
			</div>
	));

	const { userId, setUserId, userToken, setUserToken } = useContext(UserContext);
	const navigate = useNavigate();
	let [errors, setErrors] = useState([]);

	function onSubmit(e) {
			e.preventDefault();

			let formData = new FormData(e.target);
			let dict = {};
			formData.forEach((value, key) => {
					dict[key] = value;
			});

			if (dict.password !== dict.repeat_password) {
					setErrors([<p key="password-mismatch" style={{ color: 'tomato' }}>Пароли не совпадают</p>]);
					return;
			}

			delete dict.repeat_password;

			axios.post(`${SchemeHostPortOfURL}/auth/register`, dict)
					.then((res) => {
							dict['username'] = dict['email'];
							delete dict['email'];
							setUserId(res.data.id);
					})
					.catch((error) => {
							let errorsList = [];

							if (error.response.data.detail === 'REGISTER_USER_ALREADY_EXISTS') {
									errorsList.push(<p key="user-exists" style={{ color: 'tomato' }}>Этот email уже зарегистрирован</p>);
							} else if (typeof error.response.data.detail === 'string') {
									errorsList.push(<p key="server-error" style={{ color: 'tomato' }}>{error.response.data.detail}</p>);
							} else {
									error.response.data.detail.forEach((element, index) => {
											errorsList.push(<p key={`error-${index}`} style={{ color: 'tomato' }}>{element.msg}</p>);
									});
							}

							setErrors(errorsList);
					});

			let loginData = new FormData();
			loginData.append('username', dict['email']);
			loginData.append('password', dict['password']);
			axios.post(`${SchemeHostPortOfURL}/auth/jwt/login`, loginData)
					.then((res) => {
							setUserToken(res.data.access_token);
							}
					);
	}
	useEffect(()=> {
		if (userId && userToken) {
			navigate('/');
		}}, [userToken, userId])
	return (
			<div>
					<form onSubmit={onSubmit} className='form'>
							{formFields}
							{errors.length > 0 && <div className="errorList">{errors}</div>}
							<button className="buttonSubmit" type="submit">Отправить</button>
					</form>
			</div>
	);
}