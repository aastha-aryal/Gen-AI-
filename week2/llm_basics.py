import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

# Initialize the client
client = genai.Client()

# Generate text using gemini-3.5-flash
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain what a BCT (Bachelor of Computer Engineering) degree covers in 2 sentences.",
)

print(response.text)