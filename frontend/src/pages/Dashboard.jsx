import { useNavigate } from "react-router-dom";

import Navbar from "../components/Navbar";
import UploadBox from "../components/UploadBox";
import ChatBox from "../components/ChatBox";

function Dashboard() {

    const navigate = useNavigate();

    return (

        <div className="dashboard">

            <Navbar />

            <div className="dashboard-container">

                {/* Upload Section */}

                <div className="card">

                    <h2>📄 Upload Study Material</h2>

                     <ChatBox />

                </div>

                {/* Summary Button */}

                <div className="action-buttons">

                    <button
                        className="summary-btn"
                        onClick={() => navigate("/summary")}
                    >
                        📄 View Summary
                    </button>

                </div>

                {/* Chat Section */}

                <div className="card">

                    <h2>💬 Ask Questions</h2>
                     <UploadBox />
                   

                </div>

            </div>

        </div>

    );
}

export default Dashboard;