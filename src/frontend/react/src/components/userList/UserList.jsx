import getUsers from '../../queries/getUsers'
import { useQuery } from 'react-query'

import './UserList.css'


export default function UserList() {
    const {data, isLoading, isError, error} = useQuery({
        queryKey: ['user list'],
        queryFn: () => getUsers(),
    })

    // useEffect(() => {
        
    // }, [data])

    if(isLoading) {
        return('loading...')
    }

    if(isError) {
        return (error)
    }
    
    let listOfusers = []
    // for (let [_, valueObj] of Object.entries(data.data)) {
    Object.values(data.data).map((value, _) => {
        let {id, name} = value
        // listOfusers.push([id, name])
        let card = <div key={id} className="userCard">
            <p className='id'>id: {id}</p>
            <p className='name'>name: {name}</p>
        </div>
        listOfusers.push(card)
    }) 
    return (
        <div className='userCardContainer'>
            {...listOfusers}
        </div>
    )
}