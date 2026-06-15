import chromadb
from services.embedding_service import model
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="pdf_chunks"
)

def store_chunks(ids, chunks, embeddings):
    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )

    print("Stored successfully in ChromaDB")
    print("Total vectors:", collection.count())


def search_chunks(question):

    # Convert question to embedding
    question_embedding = model.encode(question)

    # Search ChromaDB
    results = collection.query(
        query_embeddings=[question_embedding.tolist()],
        n_results=1
    )

    # Print results
    

    return results["documents"][0][0]


