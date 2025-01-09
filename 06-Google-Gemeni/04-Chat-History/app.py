import google.generativeai as genai
from google.generativeai.types.generation_types import GenerateContentResponse
from google.generativeai.generative_models import ChatSession
from dotenv import load_dotenv

# Load ENV
load_dotenv()

# Initialize Model
model: GenerateContentResponse = genai.GenerativeModel("gemini-1.5-flash")

# Initialize History Variable
chat: ChatSession = model.start_chat(history=[])

# Interact with LLM (First Message)
response: GenerateContentResponse = chat.send_message("Tell me What is Kafka tell me in 1 para")
print(response.candidates[0].content.parts[0].text)

# Interact with LLM (Second Message)
response: GenerateContentResponse = chat.send_message("Tell me What Python tell me in 1 para")
print(response.candidates[0].content.parts[0].text)

# Interact with LLM (Third Message)
response: GenerateContentResponse = chat.send_message("Tell me What is Microservices tell me in 1 para")
print(response.candidates[0].content.parts[0].text)

# Interact with LLM (Fourth Message with Streaming)
response: GenerateContentResponse = chat.send_message("What is Gen AI? tell me in 1 para", stream=True)

for chunk in response:
    print(chunk.text)

# Print all Chat History
print(chat.history)

# Print all Chat History in a formated way
for message in chat.history:
    print(f"**{message.role}**: {message.parts[0].text}")
