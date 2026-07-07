from fastapi import APIRouter
from services.auth_service import register_user,login_user
from models.user_model import User,LoginUser
from utils.jwt_handler import verify_token
router = APIRouter()
from models.question_model import QuestionRequest
from utils.auth_dependency import get_current_user
@router.post("/register")
def register(user: User):
    return register_user(user)

@router.post("/login")
def login(user: LoginUser):
    return login_user(user)

from utils.auth_dependency import get_current_user
from fastapi import Depends

@router.post("/ask")
def ask_question(
    question: QuestionRequest,
    current_user = Depends(get_current_user)
):
    retrieved_context = search_chunks(
        question.question,
        user_id=current_user.id
    )