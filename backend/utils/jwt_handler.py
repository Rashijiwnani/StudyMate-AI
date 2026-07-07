from jose import jwt,JWTError

from datetime import datetime, timedelta,UTC
import os
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

print("SECRET_KEY =", SECRET_KEY)
def create_access_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.now(UTC) + timedelta(days=1)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token
print(create_access_token(1))
def verify_token(token):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        print("PAYLOAD:", payload)

        return payload

    except Exception as e:
        print("JWT ERROR:", e)
        return None