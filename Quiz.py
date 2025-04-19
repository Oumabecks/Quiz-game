import tkinter as tk
from tkinter import messagebox
import random

# Load questions from a file
def load_questions():
    # Example questions (can be replaced with file or API data)
    return [
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
        {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
        {"question": "Who wrote 'Hamlet'?", "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"], "answer": "William Shakespeare"},
        {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
        {"question": "What is the square root of 64?", "options": ["6", "7", "8", "9"], "answer": "8"},
    ]

# Function to handle the user's answer
def check_answer(selected_option):
    global current_question, score

    if selected_option == questions[current_question]["answer"]:
        score += 1
        messagebox.showinfo("Correct!", "You got it right!")
    else:
        messagebox.showinfo("Wrong!", f"The correct answer was: {questions[current_question]['answer']}")

    current_question += 1
    if current_question < len(questions):
        display_question()
    else:
        messagebox.showinfo("Quiz Over", f"Your final score is: {score}/{len(questions)}")
        reset_game()

# Function to display the current question
def display_question():
    question_label.config(text=questions[current_question]["question"])
    for i, option in enumerate(questions[current_question]["options"]):
        option_buttons[i].config(text=option, command=lambda opt=option: check_answer(opt))

# Function to reset the game
def reset_game():
    global current_question, score
    current_question = 0
    score = 0
    random.shuffle(questions)
    display_question()

# Initialize the game
questions = load_questions()
random.shuffle(questions)
current_question = 0
score = 0

# Create the main window
root = tk.Tk()
root.title("Quiz Game")
root.geometry("600x400")
root.configure(bg="#f0f8ff")  # Light blue background

# Create widgets
title_label = tk.Label(root, text="Quiz Game", font=("Arial", 24, "bold"), bg="#4682b4", fg="white")
title_label.pack(pady=10, fill=tk.X)

question_label = tk.Label(root, text="", font=("Arial", 16), bg="#f0f8ff", fg="#2f4f4f", wraplength=500, justify="center")
question_label.pack(pady=20)

button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

option_buttons = []
for i in range(4):
    btn = tk.Button(button_frame, text="", width=20, bg="#87cefa", fg="black", font=("Arial", 12), relief="raised")
    btn.grid(row=i, column=0, pady=5)
    option_buttons.append(btn)

reset_button = tk.Button(root, text="Reset Game", bg="#ffa500", fg="white", font=("Arial", 14), command=reset_game)
reset_button.pack(pady=20)

# Start the game
display_question()

# Run the application
root.mainloop()