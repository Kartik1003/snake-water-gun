import tkinter as tk
from PIL import Image, ImageTk
import random

# Initialize scores
player_score = 0
comp_score = 0

# Create main window
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("400x550")
root.config(bg="#f2f2f2")

# File paths for images
images = {
    's': "snake.jpeg",
    'w': "water.jpeg",
    'g': "gun.jpeg"
}

# Title label
tk.Label(root, text="🐍 Snake Water Gun 🔫", font=("Arial", 20, "bold"), bg="#f2f2f2").pack(pady=10)

# Score label
score_label = tk.Label(root, text="Player: 0 | Computer: 0", font=("Arial", 14), bg="#f2f2f2")
score_label.pack(pady=5)

# Frame for buttons
btn_frame = tk.Frame(root, bg="#f2f2f2")
btn_frame.pack(pady=10)

# Label to show computer's choice image
comp_img_label = tk.Label(root, bg="#f2f2f2")
comp_img_label.pack(pady=20)

# Label for result text
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f2f2f2")
result_label.pack(pady=10)

# Function to update score
def update_score(winner):
    global player_score, comp_score
    if winner == "Player":
        player_score += 1
    elif winner == "Computer":
        comp_score += 1
    score_label.config(text=f"Player: {player_score} | Computer: {comp_score}")

# Main game logic
def play(choice):
    comp_choice = random.choice(['s', 'w', 'g'])
    choices = {'s': 'Snake', 'w': 'Water', 'g': 'Gun'}

    # Show computer's image
    comp_img = Image.open(images[comp_choice]).resize((80, 80))
    comp_img_tk = ImageTk.PhotoImage(comp_img)
    comp_img_label.config(image=comp_img_tk)
    comp_img_label.image = comp_img_tk

    # Determine result
    if choice == comp_choice:
        result = "Match Draw"
        winner = "None"
    elif (choice == 's' and comp_choice == 'w') or \
         (choice == 'w' and comp_choice == 'g') or \
         (choice == 'g' and comp_choice == 's'):
        result = "You Win!"
        winner = "Player"
    else:
        result = "You Lose!"
        winner = "Computer"

    update_score(winner)
    result_label.config(text=f"Computer chose: {choices[comp_choice]}\n{result}")

# Create image buttons
def make_button(img, choice):
    img = Image.open(img).resize((60, 60))
    img_tk = ImageTk.PhotoImage(img)
    btn = tk.Button(btn_frame, image=img_tk, command=lambda: play(choice))
    btn.image = img_tk  # keep a reference!
    return btn

make_button(images['s'], 's').grid(row=0, column=0, padx=10)
make_button(images['w'], 'w').grid(row=0, column=1, padx=10)
make_button(images['g'], 'g').grid(row=0, column=2, padx=10)

# Exit button
tk.Button(root, text="Exit", font=("Arial", 12), command=root.destroy).pack(pady=10)

# Run the app
root.mainloop()
