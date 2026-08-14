import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY .env file ma bhettiena!")
    exit()

client = genai.Client(api_key=api_key)

def generate_quiz(topic):
    print(f"\n[Gemini AI] Generating 3 questions on '{topic}'...")
    
    system_instruction = (
        "You are an assistant. Generate 3 multiple choice questions on the user's requested topic. "
        "Return strictly valid JSON array of objects with keys: "
        "'question', 'options' (dictionary with keys A, B, C, D), and 'correct_option' ('A', 'B', 'C', or 'D')."
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=f"Topic: {topic}",
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.5,
                response_mime_type="application/json"
            )
        )
        return json.loads(response.text)
    except Exception as e:
        print("API Call Error:", e)
        return None

def main():
    print("===========================================")
    print("      WELCOME TO TERMINAL AI ASSISTANT     ")
    print("===========================================")
    
    # CONTINUOUS TERMINAL LOOP
    while True:
        print("\n--- Main Menu ---")
        print("1. Play a Quiz on any Topic")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == "2" or choice.lower() == "exit":
            print("\nExiting Assistant... Goodbye!")
            break
            
        elif choice == "1":
            topic = input("\nEnter quiz topic (e.g., Python, History, Football): ").strip()
            if not topic:
                topic = "General Knowledge"
                
            quiz_list = generate_quiz(topic)
            if not quiz_list:
                continue
                
            score = 0
            for idx, q in enumerate(quiz_list, 1):
                print(f"\nQ{idx}: {q['question']}")
                for opt_key, opt_val in q['options'].items():
                    print(f"  {opt_key}) {opt_val}")
                
                user_ans = input("Your answer (A/B/C/D): ").strip().upper()
                if user_ans == q['correct_option']:
                    print("🎉 Correct!")
                    score += 1
                else:
                    print(f"❌ Wrong! Correct answer: {q['correct_option']}")
            
            print(f"\n>>> Quiz Finished! Score: {score}/{len(quiz_list)} <<<")
        else:
            print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()