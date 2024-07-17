import axios from "axios";

import SchemeHostPortOfURL from '../baseSchemeHostPortOfURL'


export default async function getTasks() {
	let URL = `${SchemeHostPortOfURL}/tasks`
	return await axios.get(URL)
} 