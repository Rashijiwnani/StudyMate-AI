from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from database import get_db
from utils.auth_dependency import get_current_user
from services.pdf_services import upload_pdf_service

router = APIRouter()

@router.post("/upload")
def upload_pdf(
    pdf: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return upload_pdf_service(
        pdf,
        db,
        current_user["user_id"]
    )