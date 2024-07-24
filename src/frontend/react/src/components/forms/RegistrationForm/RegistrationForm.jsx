import '../base/Form.css'
import './RegistrationForm.css'
import SchemeHostPortOfURL from '../../../baseSchemeHostPortOfURL.js'

import { UserContext } from '../../../userContext.jsx'

import { useContext } from 'react'
import { useState } from "react"
import axios from "axios"


export default function RegistrationForm() {
	let fields = ['email', 'username', 'password', 'repeat_password']
	let formFields = []
	const	{setUserId} = useContext(UserContext)
	fields.map((value, index) => {
		
		formFields.push(<div className="formElement">
				<input key={index} type="text" name={value} style={{marginBottom: '2em', marginLeft: '2px'}}  placeholder={value} />
		</div>
	)})
	console.log('ff',formFields)


	let [errors, SetErrors] = useState([])
	
	let dict = {}
	function onSubmit(e) {
			e.preventDefault()
			
			let errorsList = []
			SetErrors([])
			let formdata = new FormData(e.target)
			for(let [d, s] of formdata.entries()) {
					dict[d] = s
			}
			if (dict.password !== dict.repeat_password) {
				SetErrors(<p style={{color: 'tomato'}}>Passwords mismatch</p>)
				return (
				<div>
					<form onSubmit={onSubmit} className='form'>
						{formFields}
						{errors && <p className="errorList">{errors}</p>}
				<button className="buttonSubmit" type="submit">submit</button>
				</form>
			</div>
			)}
			delete dict['repeat_password']
			console.log('dict dooooo', dict)
			axios.post(`${SchemeHostPortOfURL}/auth/register`, dict)
			.then((res) => {
				setUserId(res.data.id)
				delete dict['username']
				dict['username'] = dict['email']
				delete dict['email']
				let data = new FormData()
				data.append('username', dict['username'])
				data.append('password', dict['password'])
				console.log('fffsdfsdfs', data)
				axios.post(`${SchemeHostPortOfURL}/auth/jwt/login`, data)
				.then((res) => console.log(res))
				.catch((e)=>console.log('second axios error', e))
			})
			.catch((r) => {
				console.log('errrrrrrrrrrrrorrrrrrrrrrrrrr',r)
					if (r.response.data.detail === 'REGISTER_USER_ALREADY_EXISTS') {
							errorsList.push(<p style={{'color': 'tomato', 'flex': '0 0 auto'}}>this email already exists</p>)
					}

					else if (typeof(r.response.data.detail) === 'string') {
							errorsList.push(<p style={{'color': 'tomato', 'flex': '0 0 auto'}}>{r.response.data.detail}</p>)
					}
					else {
							r.response.data.detail.forEach((element) => {
									errorsList.push(<p style={{'color': 'tomato', 'flex': '0 0 auto'}}>{element.msg}</p>)
							})
					}
					SetErrors(errorsList)
			})
			// window.location.reload()
	}
	console.log('errors',errors)
	let form = 
	<div>
			<form onSubmit={onSubmit} className='form'>
					{formFields}
					{errors && <p className="errorList">{errors}</p>}
			<button className="buttonSubmit" type="submit">submit</button>
			</form>
	</div>

	return form
}