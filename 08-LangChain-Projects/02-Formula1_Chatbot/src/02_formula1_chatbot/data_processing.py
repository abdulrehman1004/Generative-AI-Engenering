import os
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain_qdrant import QdrantVectorStore
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import google.generativeai as genai
from langchain_huggingface import HuggingFaceEmbeddings


# ========================= Configuration =========================
# Environment variables for Qdrant and Gemini API
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
QDRANT_COLLECTION_NAME = "f1_gpt"

# List of URLs for Formula 1 data
F1_URLS = [
    "https://en.wikipedia.org/wiki/Formula_One",
    "https://www.formula1.com/en/latest/all",
    "https://www.forbes.com/sites/brettknight/2023/11/29/formula-1s-highest-paid-drivers-2023/?sh=12bdb942463f",
    "https://www.autosport.com/f1/news/history-of-female-f1-drivers-including-grand-prix-starters-and-test-drivers/10584871/",
    "https://en.wikipedia.org/wiki/2023_Formula_One_World_Championship",
    "https://en.wikipedia.org/wiki/2022_Formula_One_World_Championship",
    "https://en.wikipedia.org/wiki/List_of_Formula_One_World_Drivers_Champions",
    "https://en.wikipedia.org/wiki/2024_Formula_One_World_Championship",
    "https://www.formula1.com/en/results.html/2024/races.html",
    "https://www.formula1.com/en/racing/2024.html",
]

# ========================= Functions =========================


def load_documents(urls):
    """Loads documents from a list of URLs."""
    documents = []
    for url in urls:
        try:
            loader = WebBaseLoader(web_path=url)
            documents.extend(loader.load())
        except Exception as e:
            print(f"Error loading URL {url}: {e}")
    return documents


def split_documents(documents, chunk_size=1000, chunk_overlap=150):
    """Splits documents into smaller chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(documents)


def initialize_qdrant_collection(client, collection_name, vector_size):
    """Initializes or recreates a Qdrant collection."""
    try:
        client.recreate_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=vector_size, distance=Distance.COSINE)
        )
        print(f"Collection '{collection_name}' initialized successfully.")
    except Exception as e:
        print(f"Error initializing Qdrant collection '{collection_name}': {e}")


def embed_and_store_documents(documents, collection_name):
    """Generates embeddings for documents and stores them in Qdrant."""
    try:
        # Configure embedding model
        genai.configure(api_key=GEMINI_API_KEY)
        embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')

        # Store in Qdrant
        QdrantVectorStore.from_documents(
            documents=documents,
            embedding=embeddings,
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY,
            collection_name=collection_name
        )
        print("Documents successfully stored in Qdrant.")
    except Exception as e:
        print(f"Error embedding or storing documents: {e}")


# ========================= Main Execution =========================
if __name__ == "__main__":
    # Load and split documents
    documents = load_documents(F1_URLS)
    print(f"Total documents loaded: {len(documents)}")

    if documents:
        chunks = split_documents(documents)
        print(f"Total chunks created: {len(chunks)}")
        print(f"Sample chunk content:\n{chunks[0].page_content}")

        # Initialize Qdrant client
        qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

        # Create Qdrant collection
        initialize_qdrant_collection(
            client=qdrant_client,
            collection_name=QDRANT_COLLECTION_NAME,
            vector_size=384
        )

        # Embed and store document chunks
        embed_and_store_documents(
            documents=chunks,
            client=qdrant_client,
            collection_name=QDRANT_COLLECTION_NAME
        )
    else:
        print("No documents loaded. Exiting.")
