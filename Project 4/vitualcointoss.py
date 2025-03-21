import random
import tkinter as tk
from tkinter import messagebox

class CoinTossApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Coin Toss")
        self.root.geometry("400x300")
        self.root.configure(bg="#2C3E50")

        self.heads_count = 0
        self.tails_count = 0

        # Title Label
        self.title_label = tk.Label(root, text="🎲 Virtual Coin Toss 🎲", font=("Arial", 16, "bold"), fg="white", bg="#2C3E50")
        self.title_label.pack(pady=10)

        # Coin Flip Result Label
        self.result_label = tk.Label(root, text="Click 'Toss Coin' to start!", font=("Arial", 14), fg="yellow", bg="#2C3E50")
        self.result_label.pack(pady=10)

        # Toss Button
        self.toss_button = tk.Button(root, text="🎲 Toss Coin", font=("Arial", 12, "bold"), fg="white", bg="#E67E22", command=self.flip_coin)
        self.toss_button.pack(pady=10)

        # Statistics Label
        self.stats_label = tk.Label(root, text="Heads: 0 (0%) | Tails: 0 (0%)", font=("Arial", 12), fg="white", bg="#2C3E50")
        self.stats_label.pack(pady=5)

        # Reset Button
        self.reset_button = tk.Button(root, text="🔄 Reset", font=("Arial", 12, "bold"), fg="white", bg="#3498DB", command=self.reset_game)
        self.reset_button.pack(pady=5)

        # Exit Button
        self.exit_button = tk.Button(root, text="❌ Exit", font=("Arial", 12, "bold"), fg="white", bg="red", command=self.exit_game)
        self.exit_button.pack(pady=5)

    def flip_coin(self):
        """Flips the coin and updates results."""
        result = random.choice(["Heads", "Tails"])
        self.result_label.config(text=f"🎉 {result}!", fg="yellow")

        if result == "Heads":
            self.heads_count += 1
        else:
            self.tails_count += 1

        total_flips = self.heads_count + self.tails_count
        heads_percentage = (self.heads_count / total_flips) * 100 if total_flips > 0 else 0
        tails_percentage = (self.tails_count / total_flips) * 100 if total_flips > 0 else 0

        self.stats_label.config(text=f"Heads: {self.heads_count} ({heads_percentage:.2f}%) | "
                                     f"Tails: {self.tails_count} ({tails_percentage:.2f}%)")

    def reset_game(self):
        """Resets the counters and results."""
        self.heads_count = 0
        self.tails_count = 0
        self.result_label.config(text="Click 'Toss Coin' to start!", fg="white")
        self.stats_label.config(text="Heads: 0 (0%) | Tails: 0 (0%)")

    def exit_game(self):
        """Exits the application."""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

# Run the GUI
root = tk.Tk()
app = CoinTossApp(root)
root.mainloop()
