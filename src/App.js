import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import { AuthProvider } from './context/AuthContext';
import About from './pages/About';
import Homepage from './pages/Homepage';
import Login from './pages/Login';
import PrivateRoute from './utils/PrivateRoute';

const App = () => {
    return(
        <div className="App">
            <BrowserRouter>
                <AuthProvider>
                    <Routes>
                        <Route element={<Login />} path="/login" />
                        <Route element={<PrivateRoute />}>
                            <Route element={<About />} path="/about" />
                            <Route element={<Homepage />} path="/" exact />
                        </Route>
                    </Routes>
                </AuthProvider>
            </BrowserRouter>
        </div>
    )
};

export default App;