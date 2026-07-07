import { useState } from "react";
import { uploadPDF } from "../services/pdf_service";

function UploadBox() {

    const [file, setFile] = useState(null);
    const [message, setMessage] = useState("");

    const handleUpload = async () => {

        if (!file) {
            setMessage("Please select a PDF.");
            return;
        }

        try {

            const response = await uploadPDF(file);

            setMessage(response.message);

        } catch (err) {

            console.log(err);

            setMessage("Upload Failed");

        }

    };

    return (

        <div>

            <input
                type="file"
                accept=".pdf"
                onChange={(e)=>setFile(e.target.files[0])}
            />

            <button onClick={handleUpload}>
                Upload
            </button>

            <p>{message}</p>

        </div>

    );

}

export default UploadBox;



