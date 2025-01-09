import google.generativeai as genai
from google.generativeai import GenerativeModel
from google.generativeai.types.generation_types import GenerateContentResponse
from dotenv import load_dotenv

# Load ENV Variables
load_dotenv()

# Initialize model
model: GenerativeModel = genai.GenerativeModel("gemini-1.5-flash")


# # ================= Example 01 with out Stream Option =================

# Prompt to the Google Gen AI Model
response: GenerateContentResponse = model.generate_content(
    'Hey Tell me About Microservices')

# Print Whole AI Response
print(response)

# Print just main response
print(response.candidates[0].content.parts[0].text)


# ================= Example 02 with Stream Option =================
# Prompt to the Google Gen AI Model
response: GenerateContentResponse = model.generate_content(
    "Tell me the roadmap of AI Enginner", stream=True)

# Initialize an empty string to store the complete text
full_text = ''

for chunk in response:
    print(chunk.text)
    full_text += chunk.text  # Accumulate the text from each chunk

# print the complete text after the loop has finished
print(full_text)
