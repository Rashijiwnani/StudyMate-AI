import os
import fitz
from services.embedding_service import model
from models.pdf_db_model import PDF
from services.chunking_service import chunk_text
from services.chroma_service import store_chunks

def upload_pdf_service(pdf, db):

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
    
    ids = [f"chunk_{i}" for i in range(len(chunks))]

    store_chunks(ids, chunks, embeddings)

    print("Chunks:", len(chunks))
    print("Embeddings:", len(embeddings))
    print("Embedding dimensions:", len(embeddings[0]))
   
    pdf_record = PDF(
        user_id=1,
        file_name=pdf.filename,
        file_path=file_path
    )

    db.add(pdf_record)
    db.commit()

    return {
        "message": "PDF uploaded successfully",
        "filename": pdf.filename,
        "preview": text[:500],
        
    }
