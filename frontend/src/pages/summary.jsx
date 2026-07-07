import { useEffect, useState } from "react";
import axios from "axios";

function Summary() {

    const [summary, setSummary] = useState("");

    useEffect(() => {

        const fetchSummary = async () => {

            try {

                const token = localStorage.getItem("token");

                const response = await axios.get(
                    "http://127.0.0.1:8000/summary",
                    {
                        headers: {
                            Authorization: `Bearer ${token}`
                        }
                    }
                );

                setSummary(response.data.summary);

            } catch (err) {

                console.log(err);

            }

        };

        fetchSummary();

    }, []);

    return (

        <div className="summary-page">

            <h1>📘 Study Summary</h1>

            <div className="summary-card">

                <pre>{summary}</pre>

            </div>

        </div>

    );

}

export default Summary;