import chromadb
from chromadb.utils import embedding_functions
from constitution_loader import load_constitution_chunks

def init_vector_store():
    client = chromadb.Client()
    collection = client.get_or_create_collection("constitution")
    return collection

def embed_constitution(collection):
    embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    chunks = load_constitution_chunks()
    for i, chunk in enumerate(chunks):
        collection.add(documents=[chunk], ids=[f"chunk_{i}"])
    return collection

def search_context(query, collection, k=3):
    results = collection.query(query_texts=[query], n_results=k)
    return "\n\n".join(results['documents'][0])
