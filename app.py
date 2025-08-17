# 📌 Task 8 - Rule-Based Chatbot
# Objective: Create a simple chatbot using if-else statements

print("🤖 Chatbot: Hello! I am your rule-based chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("🤖 Chatbot: Hello! How can I help you today?")

    elif "your name" in user_input:
        print("🤖 Chatbot: I am a simple chatbot created using Python.")

    elif "how are you" in user_input:
        print("🤖 Chatbot: I'm doing great, thank you! How about you?")

    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M:%S")
        print(f"🤖 Chatbot: The current time is {now}")

    elif "date" in user_input:
        from datetime import datetime
        today = datetime.now().strftime("%Y-%m-%d")
        print(f"🤖 Chatbot: Today's date is {today}")

    elif "bye" in user_input:
        print("🤖 Chatbot: Goodbye! Have a great day 😊")
        break

    else:
        print("🤖 Chatbot: Sorry, I don't understand that. Can you rephrase?")
