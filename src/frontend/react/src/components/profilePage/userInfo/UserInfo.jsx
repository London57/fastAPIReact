import { useQuery } from 'react-query';
import { useContext, useEffect, useState } from 'react';
import { UserContext } from '../../../userContext.jsx';
import getThisUserInfo from '../../../queries/getThisUserInfo.js';
import {} from 'react-cookie'

export default function UserInfo() {
    const userToken = useContext(UserContext);

    const [email, setEmail] = useState('');
    const [username, setUsername] = useState('');

    const { data, isLoading, error, isError } = useQuery('userInfo', () => getThisUserInfo(userToken));
		console.log('token is', userToken)
    useEffect(() => {
        if (data) {
            setEmail(data.user.email);
            setUsername(data.user.username);
        }
    }, [data]);

    if (isLoading) {
        return <p>Загрузка...</p>;
    }

    if (isError) {
        console.log('Ошибка при получении информации о пользователе', error);
        return <p style={{ color: 'red' }}>Что-то пошло не так, попробуйте снова</p>;
    }

    return (
        <section className='userInfo'>
            <p>Email: {email}</p>
            <p>Имя пользователя: {username}</p>
        </section>
    );
}