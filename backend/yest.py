from services.chroma_service import search_chunks

results = search_chunks(
    "What is the student's CGPA?"
)

print(results)