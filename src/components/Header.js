import { useContext } from 'react';
import AuthContext from '../context/AuthContext';
import { FaBook } from 'react-icons/fa';
import { Link } from 'react-router-dom';


const Header = () => {

    let { logoutUser } = useContext(AuthContext);

    return(
        <div className="Header">
            <div>
                <h3><FaBook className="FaIcons" /> Bookstore</h3>
                <div className="linkbox">
                    <Link className="HeaderLinks" to ="/about">About</Link>
                    <p className="logout-paragraph" onClick={logoutUser}>Logout</p>
                </div>
            </div>
        </div>
    )
};

export default Header;