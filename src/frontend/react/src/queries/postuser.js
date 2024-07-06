import axios from 'axios'

export default async function postUser(body) {
    console.log('body:', body)
    let URL = 'http://localhost:8080/users'
    return await axios.post(URL, body)
}