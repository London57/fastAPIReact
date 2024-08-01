import axios from 'axios'
import SchemeHostPortOfURL from '../baseSchemeHostPortOfURL.js'


export default function getThisUserInfo(token) {
	axios.get(`${SchemeHostPortOfURL}/get_user_info`, {
		headers: {
			'Authorization': `Bearer ${token}`
		}
	})
	.then((res)=>console.log('res', res))
	.catch((r)=>console.log('r', r))
}