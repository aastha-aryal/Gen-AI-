import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

prompt = """
Explain why to choose Computer Engineering instead of other computer sciences in nepal.Answer in 10 lines only.
"""


# --------------------------------------------------
# Temperature 0.0
# --------------------------------------------------

response_low = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
    config=genai.types.GenerateContentConfig(
        temperature=0.0
    )
)

print("\n===== TEMPERATURE: 0.0 =====")
print(response_low.text)


# --------------------------------------------------
# Temperature 0.5
# --------------------------------------------------

response_medium = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
    config=genai.types.GenerateContentConfig(
        temperature=0.5
    )
)

print("\n===== TEMPERATURE: 0.5 =====")
print(response_medium.text)


# --------------------------------------------------
# Temperature 1.0
# --------------------------------------------------

response_high = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
    config=genai.types.GenerateContentConfig(
        temperature=1.0
    )
)

print("\n===== TEMPERATURE: 1.0 =====")
print(response_high.text)