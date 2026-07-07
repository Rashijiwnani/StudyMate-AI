from fastapi import APIRouter, Depends

from models.question_model import QuestionRequest
from services.chroma_service import search_chunks
from services.llm_service import generate_answer
from utils.auth_dependency import get_current_user

router = APIRouter()

@router.post("/ask")
def ask_question(
    question: QuestionRequest,
    current_user=Depends(get_current_user)
):
    retrieved_context = search_chunks(
        question.question,
        user_id=current_user["user_id"]
    )

    answer = generate_answer(
        question.question,
        retrieved_context
    )

    return {
        "answer": str(answer)
    }