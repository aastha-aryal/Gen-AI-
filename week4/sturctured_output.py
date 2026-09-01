"""
Week 4 - Day 3: Ask the model for JSON, then check it's actually valid JSON.

Free text is hard for other code to use. If we ask for JSON instead,
our program can read the answer directly instead of a human reading it.
"""

import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = "gemini-3.7-flash"

review = "The laptop arrived quickly and the battery life is amazing, but it runs a bit hot."

# Being specific about the exact JSON shape we want is the key trick here.
prompt = f"""Read this product review and return ONLY a JSON object (no extra text)
with these exact keys:
- "sentiment": "Positive", "Negative", or "Neutral"
- "key_points": a list of short strings, the main things mentioned

Review: "{review}"
"""

response = client.models.generate_content(model=MODEL, contents=prompt)
raw_text = response.text.strip()

# Models sometimes wrap JSON in ```json ... ``` fences. Strip that if present.
if raw_text.startswith("```"):
    raw_text = raw_text.strip("`")
    raw_text = raw_text.replace("json\n", "", 1)

print("Raw model output:")
print(raw_text, "\n")

# Now try to parse it as real JSON and validate it has what we expect.
try:
    data = json.loads(raw_text)

    if "sentiment" not in data or "key_points" not in data:
        print("Missing expected keys in the JSON.")
    else:
        print("Parsed successfully:")
        print("Sentiment:", data["sentiment"])
        print("Key points:", data["key_points"])

except json.JSONDecodeError:
    print("The model did not return valid JSON. Try rewording the prompt.")