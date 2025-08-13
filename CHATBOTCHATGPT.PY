# mini_ai.py

print("🤖 Hello! I am Mini AI. Type 'bye' to exit.")

# Memory to store facts
memory = {}

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("AI: Goodbye! 👋")
        break

    # If user says "my name is ___"
    if user_input.startswith("my name is"):
        name = user_input.replace("my name is", "").strip()
        memory["name"] = name
        print(f"AI: Nice to meet you, {name}!")
    
    # If user asks "what is my name"
    elif user_input == "what is my name":
        if "name" in memory:
            print(f"AI: Your name is {memory['name']}.")
        else:
            print("AI: I don't know yet! Tell me your name.")
    
    # Small Q&A
    elif "how are you" in user_input:
        print("AI: I’m doing great! Thanks for asking 😊")
    elif "time" in user_input:
        from datetime import datetime
        print("AI: Current time is", datetime.now().strftime("%H:%M:%S"))
    elif "your name" in user_input:
        print("AI: I’m Mini AI, created in Python!")
    
    else:
        print("AI: Hmm… I don’t know about that yet 🤔")
