from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

sentence = "I love playing football."

# The embedding model converts our sentence into a numerical vector
result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=sentence
)


# Get the embedding vector
embedding = result.embeddings[0].values

print("Original sentence:")
print(sentence)

print("\nEmbedding vector:")
print(embedding)

print("\nNumber of values in the vector:")
print(len(embedding))

