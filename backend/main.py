from fastapi import FastAPI
from routes.pdf_routes import router as pdf_router
from routes.auth_routes import router as auth_router
from routes.chat_routes import router as chat_router 

app = FastAPI()
app.include_router(chat_router)
app.include_router(pdf_router)
app.include_router(auth_router)

@app.get("/")
def home():
    return {
        "message": "StudyMate AI Backend Running"
    }