import { useState } from "react";
import { askQuestion } from "../services/chat_service";

function ChatBox(){

    const [question,setQuestion]=useState("");
    const [answer,setAnswer]=useState("");

    const handleSend=async()=>{

        try{

            const response=await askQuestion(question);

            setAnswer(response.answer);

        }

        catch(err){

            console.log(err);

        }

    }

    return(

        <div>

            <input

                value={question}

                onChange={(e)=>setQuestion(e.target.value)}

            />

            <button onClick={handleSend}>

                Send

            </button>

            <p>{answer}</p>

        </div>

    )

}

export default ChatBox;