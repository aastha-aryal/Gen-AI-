import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY .env file ma bhettiena!")
    exit()

client = genai.Client(api_key=api_key)

# Terminal Visual Styling
BLUE = "\033[94m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

class BCTChatbot:
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        self.model_name = model_name
        self.client = self._setup_client()

    def _setup_client(self) -> genai.Client:
        if not os.environ.get("GEMINI_API_KEY"):
            print(f"{RED}Error: GEMINI_API_KEY environment variable is missing.{RESET}")
            sys.exit(1)
        return genai.Client()

    def generate_response(self, prompt: str) -> None:
        print(f"{CYAN}{BOLD}AI:{RESET} ", end="", flush=True)
        try:
            response = self.client.models.generate_content_stream(
                model=self.model_name,
                contents=prompt
            )
            for chunk in response:
                print(chunk.text, end="", flush=True)
            print("\n")
        except APIError as e:
            print(f"\n{RED}[API Error]: Failed to reach Gemini. Details: {e}{RESET}\n")
        except Exception as e:
            print(f"\n{RED}[Error]: An unexpected issue occurred: {e}{RESET}\n")

def print_header() -> None:
    print(f"{BLUE}{'=' * 50}{RESET}")
    print(f"{BLUE}{BOLD}       BCT AI CHATBOT — WEEK 3 (DAY 1)          {RESET}")
    print(f"{BLUE}{'=' * 50}{RESET}")
    print(f"{DIM}Type 'exit' or 'quit' to end the session.{RESET}\n")

def main() -> None:
    bot = BCTChatbot()
    print_header()

    EXIT_TRIGGERS = {"exit", "quit", "q"}

    while True:
        try:
            user_input = input(f"{GREEN}{BOLD}You: {RESET}").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n\n{CYAN}AI: Goodbye! 👋{RESET}")
            sys.exit(0)

        if not user_input:
            continue

        if user_input.lower() in EXIT_TRIGGERS:
            print(f"\n{CYAN}AI: Goodbye! Have a great day! 👋{RESET}")
            break

        bot.generate_response(user_input)

if __name__ == "__main__":
    main()