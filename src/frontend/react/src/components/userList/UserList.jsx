import getUsers from '../../queries/getUsers'
import { useQuery } from 'react-query'


import './UserList.css'


export default function UserList() {
    const {data, isLoading, isError, error} = useQuery({
        queryKey: ['user list'],
        queryFn: () => getUsers(),
    })

    if(isLoading) {
        return (
            <div>loading...</div>
        )
    }

    if(isError) {
        console.log(JSON.stringify(error)
    )
        return (
           <p>Error</p>
        )
    }


    let listOfusers = []
    Object.values(data.data).map((value, _) => {
        let {id, name} = value
        // listOfusers.push([id, name])
        let card = <div className="card" style={{width: "18rem"}}>
        <img className="card-img-top" alt="Card image cap" src='...'/>
        <div className="card-body">
        <div key={id} className="userCard">
                <p className='id'>id: {id}</p>
                <p className='name'>name: {name}</p>
            </div>
        </div>
        </div>
        listOfusers.push(card)
    }) 
    return (
        <div className='userCardContainer'>
            {listOfusers}
        </div>
    )
}