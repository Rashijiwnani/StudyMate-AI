import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection("pdf_chunks")

print(collection.count())