import tkinter as tk
from PIL import Image, ImageTk
import random

class RPSGameWithImages:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors ✊🖐✌ Game")
        self.root.configure(bg="#f0f8ff")

        # Load hand images
        self.images = {
            'rock': ImageTk.PhotoImage(Image.open("rock.png").resize((100, 100))),
            'paper': ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100))),
            'scissors': ImageTk.PhotoImage(Image.open("scissors.png").resize((100, 100)))
        }

        # Score variables
        self.user_score = 0
        self.computer_score = 0
        self.draws = 0

        # Title
        self.title = tk.Label(root, text="🧠 Rock, Paper, Scissors Game", font=("Comic Sans MS", 20), bg="#f0f8ff", fg="#333")
        self.title.pack(pady=10)

        # Frames for choices
        self.choice_frame = tk.Frame(root, bg="#f0f8ff")
        self.choice_frame.pack()

        tk.Label(self.choice_frame, text="You", font=("Arial", 12), bg="#f0f8ff").grid(row=0, column=0)
        tk.Label(self.choice_frame, text="Computer", font=("Arial", 12), bg="#f0f8ff").grid(row=0, column=2)

        self.user_label = tk.Label(self.choice_frame, image=self.images['rock'], bg="#f0f8ff")
        self.user_label.grid(row=1, column=0, padx=20)

        self.vs_label = tk.Label(self.choice_frame, text="VS", font=("Arial", 14), bg="#f0f8ff")
        self.vs_label.grid(row=1, column=1)

        self.computer_label = tk.Label(self.choice_frame, image=self.images['rock'], bg="#f0f8ff")
        self.computer_label.grid(row=1, column=2, padx=20)

        # Buttons
        self.button_frame = tk.Frame(root, bg="#f0f8ff")
        self.button_frame.pack(pady=10)

        for choice in ['rock', 'paper', 'scissors']:
            btn = tk.Button(
                self.button_frame,
                image=self.images[choice],
                command=lambda c=choice: self.play(c),
                bd=2,
                bg="#d1e7dd",
                activebackground="#a5d6a7"
            )
            btn.pack(side="left", padx=10)

        # Result
        self.result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f8ff", fg="blue")
        self.result_label.pack(pady=10)

        # Score
        self.score_label = tk.Label(root, text=self.get_score_text(), font=("Arial", 12), bg="#f0f8ff", fg="#444")
        self.score_label.pack()

        # Quit button
        tk.Button(root, text="Quit", font=("Arial", 12), command=root.quit, bg="#ffcccc").pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        # Update images
        self.user_label.config(image=self.images[user_choice])
        self.computer_label.config(image=self.images[computer_choice])

        # Decide winner
        result = self.get_result(user_choice, computer_choice)
        if result == "win":
            self.user_score += 1
            text = "✅ You Win!"
        elif result == "lose":
            self.computer_score += 1
            text = "❌ You Lose!"
        else:
            self.draws += 1
            text = "🤝 It's a Draw!"

        self.result_label.config(text=f"You chose {user_choice}, Computer chose {computer_choice}. {text}")
        self.score_label.config(text=self.get_score_text())

    def get_result(self, user, comp):
        if user == comp:
            return "draw"
        elif (user == 'rock' and comp == 'scissors') or \
             (user == 'scissors' and comp == 'paper') or \
             (user == 'paper' and comp == 'rock'):
            return "win"
        else:
            return "lose"

    def get_score_text(self):
        return f"Score — You: {self.user_score} | Computer: {self.computer_score} | Draws: {self.draws}"

# Run
if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGameWithImages(root)
    root.mainloop()
