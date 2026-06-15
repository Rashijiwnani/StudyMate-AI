from fastapi import APIRouter
from services.auth_service import register_user,login_user
from models.user_model import User,LoginUser

router = APIRouter()

@router.post("/register")
def register(user: User):
    return register_user(user)

@router.post("/login")
def login(user: LoginUser):
    return login_user(user)