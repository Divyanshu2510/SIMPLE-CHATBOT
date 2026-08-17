import datetime

# ----------------------------
# Welcome Screen
# ----------------------------
print("=" * 45)
print("        SMART PYTHON CHATBOT 🤖")
print("=" * 45)

name = input("Hello! What's your name? ").strip().title()

print(f"\nWelcome, {name}! Nice to meet you. 😊")


# ----------------------------
# Help Menu
# ----------------------------
def help_menu():
    print("\n📋 You can type:")
    print("  hello")
    print("  how are you")
    print("  what is my name")
    print("  what is your name")
    print("  time")
    print("  date")
    print("  joke")
    print("  calculator")
    print("  help")
    print("  bye")


# ----------------------------
# Calculator Function
# ----------------------------
def calculator():
    print("\n🧮 Calculator Mode")
    print("Example: 10 + 5")

    expression = input("Enter calculation: ")

    try:
        result = eval(expression)
        print("✅ Result:", result)
    except:
        print("❌ Invalid calculation.")


# ----------------------------
# Chatbot Reply Function
# ----------------------------
def chatbot_reply(message, user_name):

    message = message.lower()

    if "hello" in message or "hi" in message:
        return f"Hello {user_name}! 👋"

    elif "how are you" in message:
        return "I'm doing great! Thanks for asking."

    elif "what is my name" in message or "my name" in message:
        return f"Your name is {user_name}. 😊"

    elif "what is your name" in message or "your name" in message:
        return "I'm SmartBot, your Python chatbot."

    elif "time" in message:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    elif "date" in message:
        today = datetime.datetime.now().strftime("%d %B %Y")
        return f"Today's date is {today}."

    elif "joke" in message:
        return "😂 Why do programmers prefer Python? Because it's easy to read!"

    elif "thank" in message:
        return "You're welcome! Happy to help."

    elif "help" in message:
        help_menu()
        return "Choose any command from the list."

    else:
        return "I don't understand. Type 'help' to see available commands."


# ----------------------------
# Start Chat
# ----------------------------
help_menu()

while True:

    user_message = input(f"\n{name}: ")

    if user_message.lower() == "bye":
        print(f"\nSmartBot: Goodbye, {name}! Have a wonderful day. 👋")
        break

    elif user_message.lower() == "calculator":
        calculator()

    else:
        response = chatbot_reply(user_message, name)
        print("SmartBot:", response)