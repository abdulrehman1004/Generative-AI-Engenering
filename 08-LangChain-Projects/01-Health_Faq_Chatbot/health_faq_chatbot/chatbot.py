from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Gemini 20 LLM
model: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp")

# # Invoke the model
# result = model.invoke("What is the best way to stay healthy?")

# print("Content only:")
# print(result.content)


def query_gemini(prompt: str) -> str:
    try:
        # Invoke the model
        result = model.invoke(prompt)

        return result.content
    except Exception as e:
        return str(e)


# result = query_gemini("What is the best way to stay healthy?")
# print(result)
