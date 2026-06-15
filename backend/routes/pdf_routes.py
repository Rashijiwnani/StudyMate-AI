from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from database import get_db
from services.pdf_services import upload_pdf_service

router = APIRouter()

@router.post("/upload")
def upload_pdf(
    pdf: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    return upload_pdf_service(pdf, db)