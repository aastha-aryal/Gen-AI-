import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

prompt1 = "What is BCT(Bachelors of Computer Engineering)?"

response1 = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt1
)

print("\n===== PROMPT 1 =====")
print(prompt1)

print("\nRESPONSE:")
print(response1.text)

# --------------------------------------------------
# Prompt Experiment 2
# --------------------------------------------------

prompt2 = """
Explain Computer Engineering to a first-year engineering student.
Use simple language and give a short one line answer.
"""

response2 = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt2
)

print("\n===== PROMPT 2 =====")
print(prompt2)

print("\nRESPONSE:")
print(response2.text)


# --------------------------------------------------
# Prompt Experiment 3
# --------------------------------------------------

prompt3 = """
You are an academic assistant for a Bachelor of
Computer Engineering program.

Explain what Computer Engineering students study.
Mention programming, databases, networking,
software engineering and artificial intelligence.
Keep the answer simple for each of them in one line.
"""

response3 = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt3
)

print("\n===== PROMPT 3 =====")
print(prompt3)

print("\nRESPONSE:")
print(response3.text)