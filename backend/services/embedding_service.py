from sentence_transformers import SentenceTransformer
from services.chunking_service import chunk_text
model = SentenceTransformer("all-MiniLM-L6-v2")
# chunks =chunk_text(text,chunk_size=500)
# embedding = model.encode(chunks)

# print(type(embedding))
# print(len(embedding))
# print(embedding[:10]) 