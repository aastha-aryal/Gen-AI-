from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

system_instruction = """
You are a helpful BCT college scheduling assistant.

Your job is to answer questions about Computer Engineering
college routines.

Give clear and concise answers.

Do not invent timetable information.
If the required information is not provided, say that
the information is unavailable.
"""

user_prompt = """
What is the importance of having a well-organized
college routine?
"""


response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=user_prompt,
    config=genai.types.GenerateContentConfig(
        system_instruction=system_instruction
    )
)

print("\n===== SYSTEM INSTRUCTION =====")
print(system_instruction)

print("\n===== USER PROMPT =====")
print(user_prompt)

print("\n===== AI RESPONSE =====")
print(response.text)