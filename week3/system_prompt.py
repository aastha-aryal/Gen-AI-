"""
Task 2: Basic Gemini chatbot + a system instruction.

Same as file 1, but now Gemini gets a role/personality via
`system_instruction` inside a GenerateContentConfig. This is a
standing instruction, not a turn in the conversation.

Still no memory across turns -- that's the next file.
"""

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
MODEL = "gemini-3.5-flash"

SYSTEM_INSTRUCTION = (
    "You are a friendly, patient coding tutor. Explain concepts simply, "
    "use short examples, and ask a follow-up question when it helps the "
    "user learn."
)

def main():
    print("Gemini chatbot with a personality (still no memory). Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break
        if not user_input:
            continue

        response = client.models.generate_content(
            model=MODEL,
            contents=user_input,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,  # <-- new vs file 1
            ),
        )

        print(f"Gemini: {response.text}\n")

if __name__ == "__main__":
    main()