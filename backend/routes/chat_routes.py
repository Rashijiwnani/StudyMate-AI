from fastapi import APIRouter
from models.question_model import QuestionRequest
from services.chroma_service import search_chunks
from services.llm_service import generate_answer
router = APIRouter()

@router.post("/ask")
def ask_question(question: QuestionRequest):
   retrieved_context = search_chunks(question.question)

   answer = generate_answer(
    question.question,
    retrieved_context
)

   return {
    "answer": answer
}