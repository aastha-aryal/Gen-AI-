from google import genai
from dotenv import load_dotenv
import os
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
sentences = [
    "I love playing football.",
    "Python is a programming language.",
    "I enjoy playing soccer."
]

embeddings = []                                     # Create an empty list for embeddings

# Generate an embedding for each sentence
for sentence in sentences:

    # Send the sentence to the embedding model
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=sentence
    )

    vector = result.embeddings[0].values            # Extract the numerical vector

    embeddings.append(vector)                       # Store the vector in our embeddings list

similarity_matrix = cosine_similarity(embeddings)   # Calculate similarity between all sentences

print("\nSentences:")
for i, sentence in enumerate(sentences):
    print(f"{i}: {sentence}")

print("\nSimilarity Matrix:")
print(similarity_matrix)
