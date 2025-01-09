from dotenv import load_dotenv
import google.generativeai as genai

# Load ENV Variables
load_dotenv()

# For Gen AI Configuration
genai.configure()

# List of ALL Google Gemini AI Models 
print("========= All Gemini Models =========")
for models in genai.list_models():
    print(models)
    print(models.name)


# List of ALL Google Gemini Generative Models
print("========= All Gemini Generative Models =========")
for generative_models in genai.list_models():
    if "generateContent" in generative_models.supported_generation_methods:
        print(generative_models.name)
        print(generative_models)


# List of All Google Gemini Embedding Models
print("========= All Gemini Embedding Models =========")
for embed_model in genai.list_models():
    if "embedContent" in embed_model.supported_generation_methods:
        print(embed_model)
        print(embed_model.name)
