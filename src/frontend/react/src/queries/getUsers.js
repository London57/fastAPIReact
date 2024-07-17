import axios from 'axios'

import SchemeHostPortOfURL from '../baseSchemeHostPortOfURL'


export default async function getUsers() {
    let URL = `${SchemeHostPortOfURL}/users`
    return await axios.get(URL)
}
