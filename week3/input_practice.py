import sys

# ANSI Escape Sequences for Terminal Styling
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def display_banner() -> None:
    print(f"{CYAN}{'=' * 45}{RESET}")
    print(f"{CYAN}{BOLD}       BCT CHATBOT (CLI) - STAGE 01          {RESET}")
    print(f"{CYAN}{'=' * 45}{RESET}")
    print("Commands: Type 'exit', 'quit', or press Ctrl+C to stop.\n")

def get_user_input(prompt: str = "You: ") -> str:
    try:
        return input(f"{GREEN}{BOLD}{prompt}{RESET}").strip()
    except (KeyboardInterrupt, EOFError):
        print(f"\n{RED}Session interrupted. Exiting...{RESET}")
        sys.exit(0)

def main() -> None:
    display_banner()

    EXIT_COMMANDS = {"exit", "quit", "q", ":q"}

    while True:
        user_input = get_user_input()

        if not user_input:
            continue

        if user_input.lower() in EXIT_COMMANDS:
            print(f"{RED}Goodbye! 👋{RESET}")
            break

        print(f"You entered: {user_input}\n")

if __name__ == "__main__":
    main()