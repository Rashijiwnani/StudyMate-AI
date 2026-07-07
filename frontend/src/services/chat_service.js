import axios from "axios";

const API = "http://127.0.0.1:8000";

export const askQuestion = async (question) => {

    const token = localStorage.getItem("token");

    const response = await axios.post(
        `${API}/ask`,
        {
            question
        },
        {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }
    );

    return response.data;
};