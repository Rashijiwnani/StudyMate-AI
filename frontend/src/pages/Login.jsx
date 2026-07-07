import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Login() {

    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async () => {

    const response = await axios.post(
        "http://127.0.0.1:8000/login",
        {
            email,
            password
        }
    );

    console.log("LOGIN RESPONSE:", response.data);

    if (!response.data.token) {
        alert(response.data.message);
        return;
    }

    localStorage.setItem("token", response.data.token);

    navigate("/dashboard");
};

    return (
        <div>
            <h1>Login</h1>

            <input
                placeholder="Email"
                onChange={(e) =>
                    setEmail(e.target.value)
                }
            />

            <input
                type="password"
                placeholder="Password"
                onChange={(e) =>
                    setPassword(e.target.value)
                }
            />

            <button onClick={handleLogin}>
                Login
            </button>
        </div>
    );
}

export default Login;