import tkinter as tk
import random
from datetime import datetime

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("⚔️ RPS Battle Zone")
        self.root.geometry("500x420")
        self.root.configure(bg="#EAEAEA")
        self.root.resizable(False, False)

        self.user_score = 0
        self.computer_score = 0

        # Title
        self.title_label = tk.Label(root, text="🔥 Rock, Paper, Scissors 🔥", font=("Helvetica", 22, "bold"), bg="#EAEAEA")
        self.title_label.pack(pady=20)

        # Score display
        self.score_label = tk.Label(root, text=self.get_score_text(), font=("Arial", 14), bg="#EAEAEA")
        self.score_label.pack()

        # Choices
        self.choice_frame = tk.Frame(root, bg="#EAEAEA")
        self.choice_frame.pack(pady=15)

        button_font = ("Verdana", 12)
        self.rock_button = tk.Button(self.choice_frame, text="🪨 Rock", width=10, font=button_font, command=lambda: self.play("rock"))
        self.paper_button = tk.Button(self.choice_frame, text="📄 Paper", width=10, font=button_font, command=lambda: self.play("paper"))
        self.scissors_button = tk.Button(self.choice_frame, text="✂️ Scissors", width=10, font=button_font, command=lambda: self.play("scissors"))

        self.rock_button.grid(row=0, column=0, padx=8)
        self.paper_button.grid(row=0, column=1, padx=8)
        self.scissors_button.grid(row=0, column=2, padx=8)

        # Result
        self.result_label = tk.Label(root, text="Make your move!", font=("Arial", 14), fg="black", bg="#EAEAEA", wraplength=480)
        self.result_label.pack(pady=18)

        # Time bar
        self.time_label = tk.Label(root, text="", font=("Arial", 10), fg="gray", bg="#EAEAEA")
        self.time_label.pack()

        # Reset
        self.reset_button = tk.Button(root, text="🔄 Reset Game", font=("Arial", 12), width=16, command=self.reset_game)
        self.reset_button.pack(pady=10)

    def get_score_text(self):
        return f"🧍 You: {self.user_score}   🤖 Computer: {self.computer_score}"

    def play(self, user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        result = self.determine_winner(user_choice, computer_choice)

        if result == "user":
            self.user_score += 1
            outcome = "🎉 You win this round!"
        elif result == "computer":
            self.computer_score += 1
            outcome = "😅 Computer wins this round!"
        else:
            outcome = "🤝 It's a tie!"

        now = datetime.now().strftime("%I:%M:%S %p")
        self.score_label.config(text=self.get_score_text())
        self.result_label.config(text=f"You chose {user_choice}, computer chose {computer_choice}. {outcome}")
        self.time_label.config(text=f"Last move: {now}")

    def determine_winner(self, user, computer):
        if user == computer:
            return "tie"
        elif (user == "rock" and computer == "scissors") or \
             (user == "scissors" and computer == "paper") or \
             (user == "paper" and computer == "rock"):
            return "user"
        else:
            return "computer"

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text=self.get_score_text())
        self.result_label.config(text="Game has been reset. Make your move!")
        self.time_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()