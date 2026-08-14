import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

# Grounding context provided directly in context window
bct_routine_context = """
BCT III/I Routine (Sample Data):
- Monday: 10:15 - 12:45 | Engineering Economics (Lect) | Room 301
- Monday: 01:30 - 04:00 | Computer Networks Lab | Group A (Lab 2)
- Tuesday: 10:15 - 11:55 | Operating System (Lect) | Room 301
- Wednesday: 10:15 - 12:45 | Artificial Intelligence (Lect) | Room 302
"""

system_instruction = f"""
You are an official BCT Routine Assistant.
Answer questions strictly based on the routine provided below.
If a requested schedule is not present in the context, respond with "Information unavailable in schedule."

=== ROUTINE DATA ===
{bct_routine_context}
"""

query = "What class do I have on Monday afternoon?"

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=query,
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.0
    )
)

print(f"Query: {query}\nResponse:\n{response.text}")