import os
import fitz
from services.embedding_service import model
from models.pdf_db_model import PDF
from services.chunking_service import chunk_text
from services.chroma_service import store_chunks
from services.summary_service import generate_summary

def upload_pdf_service(pdf, db,user_id):

    UPLOAD_DIR = os.path.join(os.getcwd(), "uploads")
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, pdf.filename)

    with open(file_path, "wb") as file:
        file.write(pdf.file.read())

    doc = fitz.open(file_path)

    text = ""

    for page in doc:
        text += page.get_text()
        # 👇 Add chunking here
    chunks = chunk_text(text)
    embeddings = model.encode(chunks)
    summary = generate_summary(text)
    import uuid

    ids = [
    str(uuid.uuid4())
    for _ in chunks]

    store_chunks(
    ids,
    chunks,
    embeddings,
    user_id=user_id      
)
    print("Chunks:", len(chunks))
    print("Embeddings:", len(embeddings))
    print("Embedding dimensions:", len(embeddings[0]))
   
    pdf_record = PDF(
        user_id=user_id,
        file_name=pdf.filename,
        file_path=file_path,
        summary= summary
    )

    db.add(pdf_record)
    db.commit()
    
    return {
        "message": "PDF uploaded successfully",
        "filename": pdf.filename,
        # "preview": text[:500],
        "summary": summary
    }
