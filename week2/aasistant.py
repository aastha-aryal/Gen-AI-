import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

system_instruction = """
You are a helpful BCT college scheduling assistant.
Your job is to answer questions about Computer Engineering college routines.
Give clear and concise answers.
Do not invent timetable information.
If the required information is not provided, say that the information is unavailable.
"""

print("=== BCT Assistant Online (Type 'exit' or 'quit' to stop) ===")

# Infinite loop suru gareko terminal ma continuous sodhna
while True:
    # Terminal ma user bata input line
    user_prompt = input("\nYou: ")
    
    # User le exit lekhyo bhane program stop garne
    if user_prompt.lower() in ["exit", "quit"]:
        print("Assistant: Goodbye!")
        break
    
    # Response generate garne
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction
        )
    )
    
    # Result display garne
    print(f"Assistant: {response.text}")