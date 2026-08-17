def reply(message):

    if message == "hello":
        return "Hello!"

    elif message == "python":
        return "Python is a programming language."

    elif message == "bye":
        return "Goodbye!"

    else:
        return "I don't know that."


print("Simple Chatbot Started")

while True:

    user = input("You: ").lower()

    answer = reply(user)

    print("Bot:", answer)

    if user == "bye":
        break