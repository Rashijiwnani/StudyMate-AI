import axios from "axios";

const API = "http://127.0.0.1:8000";

export const uploadPDF = async (file) => {

    const formData = new FormData();

    formData.append("pdf", file);

    const token = localStorage.getItem("token");

    const response = await axios.post(
        `${API}/upload`,
        formData,
        {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }
    );

    return response.data;
};