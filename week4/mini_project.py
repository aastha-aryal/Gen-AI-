"""
Week 4 - Day 4-5: Mini Project - Text Summarizer.

Takes any plain text the user pastes in, and asks the model to
summarize it in 2-3 sentences. This is the "one useful task" mini
project required by the assignment.
"""

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = "gemini-3.7-flash"


def summarize(text: str) -> str:
    prompt = f"""Summarize the following text in 2-3 clear sentences.
Keep only the most important information, in plain simple language.

Text:
{text}
"""
    response = client.models.generate_content(model=MODEL, contents=prompt)
    return response.text


def main():
    print("=== Text Summarizer ===")
    print("Paste the text you want summarized, then press Enter twice.\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = "\n".join(lines)

    if not text.strip():
        print("No text entered.")
        return

    print("\nSummary:")
    print(summarize(text))


if __name__ == "__main__":
    main()


# --- Sample input/output for the report -------------------------------------
# Sample input:
# "Nepal's tourism sector saw a strong rebound this year, with trekking routes
#  in the Annapurna and Everest regions reporting record visitor numbers. Local
#  guides say better weather forecasting and improved trail infrastructure have
#  made multi-day treks safer and more accessible for first-time visitors.
#  However, some conservationists have raised concerns about the environmental
#  impact of the increased foot traffic on fragile mountain ecosystems."
#
# Sample output (example):
# "Nepal's tourism industry has rebounded strongly, driven by record trekking
#  visits to Annapurna and Everest thanks to better forecasting and trail
#  infrastructure. However, conservationists warn the rise in foot traffic may
#  harm fragile mountain ecosystems."