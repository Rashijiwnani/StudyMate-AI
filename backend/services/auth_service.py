from models.user_db_model import UserDB
from database import SessionLocal
import bcrypt
from utils.jwt_handler import create_access_token

def register_user(user):
    session = SessionLocal()

    try:
        existing_user = session.query(UserDB)\
                               .filter(UserDB.email == user.email)\
                               .first()

        if existing_user is not None:
            return {"message": "Email already exists"}

        hashed_password = bcrypt.hashpw(
            user.password.encode(),
            bcrypt.gensalt()
        ).decode()

        new_user = UserDB(
            name=user.name,
            email=user.email,
            password=hashed_password
        )

        session.add(new_user)
        session.commit()

        return {
            "message": f"Welcome {user.name}",
            "email": user.email
        }

    finally:
        session.close()

def login_user(user):
    session = SessionLocal()

    try:
        db_user = session.query(UserDB)\
                         .filter(UserDB.email == user.email)\
                         .first()

        if db_user is None:
            return {"message": "User not found"}
        print("Email:", user.email)
        print("Password from DB:", repr(db_user.password))
        print("Type:", type(db_user.password))
        if not bcrypt.checkpw(
            user.password.encode(),
            db_user.password.encode()
        ):
            return {"message": "Invalid password"}
    
        token = create_access_token(db_user.id)

        return {
    "message": f"Welcome back {db_user.name}",
    "token": token,
    "user_id": db_user.id
}
    finally:
        session.close()