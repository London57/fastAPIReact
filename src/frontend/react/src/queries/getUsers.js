import axios from 'axios'

export default async function getUsers() {
    let URL = 'http://localhost:8080/users'
    const data = await axios.get(URL)
    return data
}
