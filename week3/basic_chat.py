"""
Task 1 ONLY: Basic command line chatbot using Gemini.

Sends whatever the user types to Gemini and prints the response.
No system instruction, no memory of earlier turns yet.
"""

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()  # reads .env in the current folder into environment variables

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
MODEL = "gemini-3.5-flash"


def main():
    print("Basic Gemini chatbot (no memory, no personality yet). Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break
        if not user_input:
            continue

        # A single, standalone call -- nothing here knows about earlier turns.
        response = client.models.generate_content(
            model=MODEL,
            contents=user_input,
        )

        print(f"Gemini: {response.text}\n")


if __name__ == "__main__":
    main()