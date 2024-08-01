import '../base/Form.css'
import './RegistrationForm.css'
import SchemeHostPortOfURL from '../../../baseSchemeHostPortOfURL.js'

import { UserContext } from '../../../userContext.jsx'

import { useContext, useState, useEffect, useRef } from 'react'
import axios from "axios"

import { useNavigate } from 'react-router-dom'

import {} from 'react-cookie'


export default function RegistrationForm() {
	let fields = ['email', 'username', 'password', 'repeat_password'];
	let dict = {};
	const navigate = useNavigate();
	let [errors, setErrors] = useState([]);
	const { userId, setUserId, userToken, setUserToken } = useContext(UserContext);
	const reference = useRef(true)

	let formFields = fields.map((value, index) => (
			<div className="formElement" key={index}>
					<input type="text" name={value} style={{ marginBottom: '2em', marginLeft: '2px' }} placeholder={value} />
			</div>
	));

	function onSubmit(e) {
		e.preventDefault();

		let formData = new FormData(e.target);
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
						console.log('errrorrrererer', error)
						if (error.response.data?.detail === 'REGISTER_USER_ALREADY_EXISTS') {
								errorsList.push(<p key="user-exists" style={{ color: 'tomato' }}>this email already exists</p>);
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
				loginData.forEach((value, key) => {
					console.log(value, key)
				});
				axios.post(`${SchemeHostPortOfURL}/auth/jwt/login`, loginData)
						.then((res) => {
							console.log(res)
								// setUserToken(res.data.access_token);
							}
						)	
						.catch((r) => {
							console.log(r)
							setErrors(<p style={{color: 'red'}}>Something went wrong, please, try again</p>)
						})
	}
	// useEffect(()=> {
	// 	if(reference.current) {
	// 		reference.current = false;
	// 	}
	// 	else {
	// 		console.log('in uEff', dict)

	// }})
	useEffect(()=> {
		if (userId && userToken) {
			navigate('/');
		}}, [userToken, userId])
	return (
			<div>
					<form onSubmit={onSubmit} className='form'>
							{formFields}
							{errors && <div className="errorList">{errors}</div>}
							<button className="buttonSubmit" type="submit">Отправить</button>
					</form>
			</div>
	);
}