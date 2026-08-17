
import tkinter as tk
from tkinter import scrolledtext
import datetime

window = tk.Tk()
window.title("Smart Python Chatbot")
window.geometry("500x650")
window.configure(bg="#0F172A")
window.resizable(False, False)

title = tk.Label(
    window,
    text="🤖 SmartBot",
    bg="#1E293B",
    fg="white",
    font=("Helvetica",18,"bold"),
    pady=15
)
title.pack(fill="x")

chat_area = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    font=("Arial",11),
    bg="#111827",
    fg="white",
    bd=0
)
chat_area.pack(padx=10,pady=10,fill="both",expand=True)
chat_area.insert(tk.END,"SmartBot: Hello! What's your name?\n\n")
chat_area.config(state="disabled")

bottom = tk.Frame(window,bg="#0F172A")
bottom.pack(fill="x",padx=10,pady=10)

user_input = tk.Entry(
    bottom,
    font=("Arial",12),
    bg="#1F2937",
    fg="white",
    insertbackground="white",
    bd=0
)
user_input.pack(side="left",fill="x",expand=True,ipady=10)

user_name = None

def bot_reply(message):
    global user_name
    msg = message.lower()

    if user_name is None:
        user_name = message.title()
        return f"Nice to meet you, {user_name}! 😊"

    if "hello" in msg:
        return f"Hello {user_name}!"
    elif "my name" in msg:
        return f"Your name is {user_name}."
    elif "your name" in msg:
        return "I'm SmartBot."
    elif "time" in msg:
        return "Current time: " + datetime.datetime.now().strftime("%I:%M %p")
    elif "date" in msg:
        return datetime.datetime.now().strftime("%d %B %Y")
    elif "joke" in msg:
        return "Why do programmers love Python? Because it's easy to read!"
    elif "bye" in msg:
        return f"Goodbye {user_name}! 👋"
    else:
        return "Try: hello, time, joke, my name"

def send_message():
    message = user_input.get().strip()

    if message == "":
        return

    chat_area.config(state="normal")
    chat_area.insert(tk.END,f"You: {message}\n")

    response = bot_reply(message)

    chat_area.insert(tk.END,f"SmartBot: {response}\n\n")
    chat_area.config(state="disabled")

    user_input.delete(0,tk.END)
    chat_area.yview(tk.END)

send_button = tk.Button(
    bottom,
    text="Send",
    command=send_message,
    bg="#2563EB",
    fg="white",
    font=("Arial",10,"bold"),
    bd=0,
    padx=20
)
send_button.pack(side="right",padx=8)

user_input.bind("<Return>", lambda event: send_message())

window.mainloop()