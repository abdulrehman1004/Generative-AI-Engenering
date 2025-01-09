import google.generativeai as genai
from google.generativeai.types.generation_types import GenerateContentResponse
from google.generativeai.generative_models import ChatSession
from dotenv import load_dotenv

load_dotenv()

response = genai.embed_content(
    model="models/text-embedding-004",
    content="What is Full Stack Development?",
    task_type="retrieval_document",
    title="Embedding of single string"
)

print(response)

# 1 input > 1 vector output
print(str(response["embedding"])[:150], "... TRIMMED]")

result = genai.embed_content(
    model="models/text-embedding-004",
    content=[
        "What is the meaning of life?",
        "How much wood would a woodchuck chuck?",
        "How does the brain work?",
    ],
    task_type="retrieval_document",
    title="Embedding of list of strings",
)

print(response)

# A list of inputs > A list of vectors output
for v in result["embedding"]:
    print(str(v)[:50], "... TRIMMED ...")
