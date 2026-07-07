from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.pdf_routes import router as pdf_router
from routes.auth_routes import router as auth_router
from routes.chat_routes import router as chat_router
from routes.summary_routes import router as summary_router
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(pdf_router)
app.include_router(auth_router)
app.include_router(summary_router)
@app.get("/")
def home():
    return {
        "message": "StudyMate AI Backend Running"
    }