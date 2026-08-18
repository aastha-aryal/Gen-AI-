"""
Task 4 / Integration: everything from files 1-3, combined, plus
temperature and max_output_tokens exposed as constants so you can
experiment and observe the effect on responses.

This is the file you'd hand in as "the deliverable" -- 01/02/03
were the learning steps that built up to it.
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

# --- Parameters to experiment with ------------------------------------------
# TEMPERATURE: 0 = focused/deterministic (same prompt -> near-identical
#              answers). Closer to 1+ = more varied/creative wording.
# MAX_OUTPUT_TOKENS: hard cap on reply length. If Gemini hits this limit
#              mid-sentence, the reply just stops -- it does not
#              summarize itself to fit.
TEMPERATURE = 0.7
MAX_OUTPUT_TOKENS = 500

chat = client.chats.create(
    model=MODEL,
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTION,
        temperature=TEMPERATURE,
        max_output_tokens=MAX_OUTPUT_TOKENS,
    ),
)


def main():
    print(f"Gemini chatbot ready. temperature={TEMPERATURE}, max_output_tokens={MAX_OUTPUT_TOKENS}")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break
        if not user_input:
            continue

        response = chat.send_message(user_input)
        print(f"Gemini: {response.text}\n")


if __name__ == "__main__":
    main()

# --- How to run the parameter experiment for your write-up -----------------
# 1. Pick one fixed prompt, e.g. "Write an opening line for a mystery novel."
# 2. Set TEMPERATURE = 0, run it 3 times -> replies should look almost the same.
# 3. Set TEMPERATURE = 1.0, run it 3 times -> replies should vary more.
# 4. Set MAX_OUTPUT_TOKENS = 20, ask something needing a long answer -> reply
#    gets cut off abruptly (not neatly summarized).
# 5. Raise MAX_OUTPUT_TOKENS back to 500+ and compare.
# Write down what you actually saw -- that's your "short note" deliverable.