import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY .env file ma bhettiena!")
    exit()

client = genai.Client(api_key=api_key)

def get_5_quizzes_from_api():
    print("Gemini API is generating 5 questions... Please wait!\n")
    
    # Prompting API to generate 5 questions in a JSON array
    system_instruction = (
        "You are a quiz generator. Generate exactly 5 unique multiple choice general knowledge questions. "
        "Return strictly a valid JSON array of 5 objects. Each object must have keys: "
        "'question', 'options' (dictionary with keys A, B, C, D), and 'correct_option' ('A', 'B', 'C', or 'D')."
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Generate 5 fun general knowledge questions.",
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.7,
                response_mime_type="application/json"
            )
        )
        return json.loads(response.text)
    except Exception as e:
        print("API Call Error:", e)
        return None

def start_quiz():
    quiz_list = get_5_quizzes_from_api()
    
    if not quiz_list:
        print("Quiz load garna sakiena.")
        return

    score = 0
    total_questions = len(quiz_list)

    print("=== GEMINI 5-QUESTION QUIZ GAME ===")

    for idx, quiz in enumerate(quiz_list, start=1):
        print(f"\n-----------------------------------")
        print(f"Question {idx} of {total_questions}: {quiz['question']}\n")
        
        # Display options A, B, C, D
        for option_key, option_text in quiz['options'].items():
            print(f"  {option_key}) {option_text}")
        
        # Take user input
        user_answer = input("\nSelect your answer (A / B / C / D): ").strip().upper()
        correct = quiz['correct_option'].upper()
        
        # Validate and calculate score
        if user_answer == correct:
            print("🎉 Correct Answer!")
            score += 1
        else:
            print(f"❌ Incorrect! Correct Answer was: {correct} ({quiz['options'].get(correct, '')})")

    # Final Score Display
    print("\n===================================")
    print(f"QUIZ FINISHED! Your Final Score: {score}/{total_questions}")
    print("===================================\n")

if __name__ == "__main__":
    start_quiz()