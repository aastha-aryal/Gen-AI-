"""
Week 4 - Day 1-2: Three ways to write a prompt.

We ask the model to do ONE task (classify a message's sentiment)
three different ways, so we can compare the outputs.
"""

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = "gemini-3.7-flash"

message = "The delivery was late again and no one replied to my emails."


def ask(prompt):
    response = client.models.generate_content(model=MODEL, contents=prompt)
    return response.text


# 1. Zero-shot: just ask directly, no examples.
zero_shot_prompt = f"Classify the sentiment of this message as Positive, Negative, or Neutral:\n{message}"

# 2. Few-shot: show a few examples first, so the model copies the pattern.
few_shot_prompt = f"""Classify sentiment as Positive, Negative, or Neutral.

Message: "I love how fast this app is!" -> Positive
Message: "The screen is fine, nothing special." -> Neutral
Message: "This is the third time my order has been wrong." -> Negative

Message: "{message}" ->"""

# 3. Chain-of-thought: ask the model to reason step by step first.
cot_prompt = f"""Classify the sentiment of this message as Positive, Negative, or Neutral.
First explain your reasoning in one line, then write the final answer
on its own line as: Final answer: <sentiment>

Message: "{message}"
"""

print("=== Zero-shot ===")
print(ask(zero_shot_prompt), "\n")

print("=== Few-shot ===")
print(ask(few_shot_prompt), "\n")

print("=== Chain-of-thought ===")
print(ask(cot_prompt), "\n")