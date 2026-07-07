from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.pdf_db_model import PDF
from utils.auth_dependency import get_current_user

router = APIRouter()

@router.get("/summary")
def get_summary(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    pdf = (
        db.query(PDF)
        .filter(PDF.user_id == current_user["user_id"])
        .order_by(PDF.id.desc())
        .first()
    )

    if not pdf:
        return {
            "message": "No PDF uploaded."
        }

    return {
        "summary": pdf.summary
    }