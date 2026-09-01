from google import genai
from dotenv import load_dotenv
import os
from sklearn.metrics.pairwise import cosine_similarity      # This function calculates how similar two vectors are

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

sentence1 = "I love playing football."
sentence2 = "I enjoy playing soccer."

result1 = client.models.embed_content(
    model="gemini-embedding-001",
    contents=sentence1
)
vector1 = result1.embeddings[0].values


result2 = client.models.embed_content(
    model="gemini-embedding-001",
    contents=sentence2
)
vector2 = result2.embeddings[0].values

#Calculate cosine similarity
# sklearn expects the vectors inside another list

similarity = cosine_similarity([vector1], [vector2])

print("Sentence 1:")
print(sentence1)

print("\nSentence 2:")
print(sentence2)

print("\nCosine Similarity:")
print(similarity[0][0])
