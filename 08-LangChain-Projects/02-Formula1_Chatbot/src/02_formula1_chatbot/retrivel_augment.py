from langchain_huggingface import HuggingFaceEmbeddings
import os
from qdrant_client import QdrantClient
from langchain_community.vectorstores import Qdrant
import google.generativeai as genai

# ========================= Configuration =========================
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
QDRANT_COLLECTION_NAME = "f1_gpt"

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Initialize Qdrant client
qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

# Connect to Qdrant vector store
qdrant = Qdrant(
    client=qdrant_client,
    collection_name=QDRANT_COLLECTION_NAME,
)

# Query for information
query = "Who is the highest-paid F1 driver?"

# ========================== Data Retrieval ==========================


def retrieve_data(query, k=5):
    """Retrieve top-k relevant results from the Qdrant vector store."""
    try:
        results = qdrant.similarity_search(query, k=k)
        if not results:
            print("No results found for the query.")
            return None
        print(f"Top {k} results retrieved successfully.")
        for i, result in enumerate(results, 1):
            print(f"\nResult {i}:")
            print(f"Content: {result.page_content}")
        return results
    except Exception as e:
        print(f"Error retrieving data: {e}")
        return None


# ========================== Execution ==========================
if __name__ == "__main__":
    print("Retrieving data from the knowledge base...\n")
    retrieve_data(query=query, k=5)


# # ========================= Functions =========================


# def create_retrieval_chain():
#     """Creates a Retrieval-Augmented Generation chain."""
#     # Initialize Qdrant client
#     qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

#     # Connect to Qdrant vector store
#     vector_store = Qdrant(
#         client=qdrant_client,
#         collection_name=QDRANT_COLLECTION_NAME,
#     )

#     # Define the LLM
#     llm = GooglePalm(model="text-bison-001", api_key=GEMINI_API_KEY)

#     # Define a prompt template
#     prompt_template = PromptTemplate(
#         input_variables=["context", "question"],
#         template="""
# You are an expert on Formula 1. Based on the following context, answer the question as accurately as possible.

# Context:
# {context}

# Question:
# {question}

# Answer:"""
#     )

#     # Create a RetrievalQA chain
#     chain = RetrievalQA.from_chain_type(
#         llm=llm,
#         retriever=vector_store.as_retriever(search_kwargs={"k": 5}),
#         return_source_documents=True,
#         chain_type_kwargs={"prompt": prompt_template},
#     )

#     return chain


# def handle_query(chain, query):
#     """Handles the query and retrieves the response."""
#     result = chain.run(query)
#     return {
#         "answer": result["result"],
#         "sources": result["source_documents"],
#     }


# Environment variables for Qdrant and Gemini API
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_COLLECTION_NAME = "f1_gpt"

# Initialize Qdrant client
qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
# Initialize the embedding model
embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')


def search_vectors(client, collection_name, user_query, top_k=5):
    """
    Search for vectors in the Qdrant database based on a user query.
    Args:
        client: Qdrant client instance.
        collection_name: Name of the Qdrant collection.
        user_query: The query text provided by the user.
        top_k: Number of top results to retrieve.
    Returns:
        List of matching results with metadata.
    """
    try:
        # Embed the user query
        query_embedding = embeddings.embed_text(user_query)

        # Perform the search
        search_results = client.search(
            collection_name=collection_name,
            query_vector=query_embedding,
            limit=top_k,  # Number of results to retrieve
        )

        # Return the results
        return [
            {
                "id": result.id,
                "score": result.score,
                "content": result.payload.get("content", ""),
                "url": result.payload.get("url", ""),
            }
            for result in search_results
        ]
    except Exception as e:
        print(f"Error during search: {e}")
        return []
