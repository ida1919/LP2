import re
import random

# Patterns
response_patterns = [
    (r'\b(hi|hello|hey)\b',
     ["Hello! How can I help you?",
      "Hi! What do you need?",
      "Hey there!"]),

    (r'\b how are you\b',
     ["I am fine! What about you?",
      "Doing great! How are you?"]),

    (r'\bwhat is your name\b|\bwho are you\b',
     ["I am SmartBot, your assistant.",
      "You can call me SmartBot!"]),

    (r'\bai\b|\bartificial intelligence\b',
     ["AI means machines can think like humans.",
      "Artificial Intelligence helps machines learn."]),

    (r'\bjoke\b',
     ["Why did the computer sleep? Because it had too many tabs open ",
      "Why do coders hate nature? Too many bugs!"]),

    (r'\bthank(s| you)\b',
     ["Welcome!", "No problem!", "Glad to help!"]),

    (r'\b(bye|exit|quit)\b',
     ["Bye! Take care!",
      "Goodbye!",
      "See you soon!"]),

    (r'.*',
     ["I did not understand. Try again.",
      "Can you rephrase that?",
      "Ask me about time, jokes, or math."])
]

# -------- RESPONSE FUNCTION --------
def chatbot_reply(user_text):
    text = user_text.lower().strip()

    # Pattern matching
    for pattern, replies in response_patterns:
        if re.search(pattern, text):
            return random.choice(replies)

    return "I don't know how to respond."

# ---------------- MAIN ----------------
if  __name__ == "__main__":
    print("=" * 40)
    print("        Welcome to SmartBot")
    print("        Type 'bye' to exit")
    print("=" * 40)

while True:
    user_text = input("\nYou : ").strip().lower()

    if user_text in ["bye", "exit", "quit"]:
        print("Bot : Goodbye!")
        break

    elif user_text:
        print("Bot :", chatbot_reply(user_text))

    else:
        print("Please type something!")
