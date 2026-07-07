import chromadb
from services.embedding_service import model
import os 

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="pdf_chunks"
)


print("Current dir:", os.getcwd())
print("Absolute path:", os.path.abspath("chroma_db"))
def store_chunks(ids, chunks, embeddings, user_id):

    collection.add(
    documents=chunks,
    embeddings=embeddings,
    ids=ids,
    metadatas=[
        {
            "user_id": user_id
        }
        for _ in chunks
    ]
)
    # print(collection.get())
    # print("Stored successfully in ChromaDB")
    # print("Total vectors:", collection.count())

def search_chunks(question, user_id):
    
    # Convert question to embedding
    question_embedding = model.encode(question)

    # Search ChromaDB
    results = collection.query(
        query_embeddings=[question_embedding.tolist()],
        n_results=3,
        where={"user_id": user_id}
        
    )

    # print(results)
    # print("Total vectors:", collection.count())

    context = "\n".join(results["documents"][0])

    return context

