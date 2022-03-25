import { useContext } from 'react';
import AuthContext from '../context/AuthContext';

const Login = () => {

    let { loginUser } = useContext(AuthContext);

    return(
        <div className="Login">
            <form onSubmit={loginUser}>
                <input type="text" name="email" placeholder="Enter mailadress ..." autoFocus />
                <input type="password" name="password" placeholder="Enter password ..." autoComplete="true"/>
                <input type="submit" value="Einloggen" />
            </form>
        </div>
    )

};

export default Login;