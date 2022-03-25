import axios from 'axios';
import jwt_decode from 'jwt-decode';
import dayjs from 'dayjs';
import { useContext } from 'react';
import AuthContext from '../context/AuthContext';


const baseURL = 'http://localhost:8000';

const useAxios = () => {

    const { authTokens, setAuthTokens, setUser } = useContext(AuthContext);

    const AxiosInstance = axios.create({
        baseURL: baseURL,
        headers : {
            'Authorization': `JWT ${String(authTokens.access)}`,
        }
    });

    AxiosInstance.interceptors.request.use(async (req) => {
    
        // get user from token (with decoding) and check if token is expired -> if not: return
        const user = jwt_decode(authTokens.access);
        const isExpired = dayjs.unix(user.exp).diff(dayjs()) < 1;
        if (!isExpired) return req;
    
        // if token is expired, get new token (access & refresh) with call to refresh token and set it to local storage and header
        const response = await axios.post(`${baseURL}/api/token/refresh/`, {
            refresh: authTokens.refresh,
        });
        localStorage.setItem('authTokens', JSON.stringify(response.data));

        // updating different states
        setAuthTokens(response.data);
        setUser(response.data.access);

        req.headers.Authorization = `JWT ${response.data.access}`;
    
        return req;
    });

    return AxiosInstance;
};

export default useAxios;