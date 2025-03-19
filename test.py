import customtkinter as ctk
from tkinter import PhotoImage
from PIL import Image, ImageTk  # Import Pillow for image resizing
import random
import time

app = ctk.CTk()
app.title("Rock-Paper-Scissors")
app.geometry("900x700")
app.resizable(False,False)
app.configure(fg_color="#ade8f4")  # Light gray background

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

player_choice = None
computer_choice = None

player_score = 0
computer_score = 0
tie_score = 0
def load_and_resize_image(file_path, width, height):
    img = Image.open(file_path)
    img = img.resize((width, height), Image.Resampling.LANCZOS)  # Resize image
    return ImageTk.PhotoImage(img)
def home_screen():
    for widget in app.winfo_children():
        widget.destroy()

    # Title
    label = ctk.CTkLabel(app, text="Rock-Paper-Scissors", font=("Poppins ExtraBold", 40, "bold"), text_color="#334195")
    label.pack(pady=20)

    # Description
    description = (
        "Welcome to the classic game of Rock-Paper-Scissors!\n"
        " Test your luck and skills against the computer 🎮\n"
        "Choose wisely: Rock smashes Scissors, Scissors cut Paper, and Paper wraps Rock.\n"
        "Click 'Start Game' below to begin your adventure!"
    )
    desc_label = ctk.CTkLabel(app, text=description, font=("Poppins", 18), text_color="#555555", wraplength=500, justify="center")
    desc_label.pack(pady=20)

    # Start Button
    start_button = ctk.CTkButton(app, text="Start Game",  font=("Poppins ExtraBold", 25), fg_color="#334195", hover_color="#556dcf", width=200,command=game_screen)
    start_button.pack(pady=40,padx=40)

def clearwid():
    for widget in app.winfo_children():
        widget.destroy()

def game_screen():
    clearwid()
    # Title
    global player_score_label, computer_score_label,tie_score_label

    label = ctk.CTkLabel(app, text="Choose Your Option", font=("Poppins ExtraBold", 25), text_color="#334195")
    label.pack(pady=10)

    score_frame = ctk.CTkFrame(app, fg_color="#caf0f8", corner_radius=10)
    score_frame.pack(pady=10)

    player_score_label = ctk.CTkLabel(score_frame, text=f"Player Score: {player_score}", font=("Poppins ExtraBold", 18, "bold"),
                                      text_color="#334195")
    player_score_label.grid(row=0, column=0, padx=20, pady=5)

    computer_score_label = ctk.CTkLabel(score_frame, text=f"Computer Score: {computer_score}",
                                        font=("Poppins ExtraBold", 18, "bold"), text_color="#334195")
    computer_score_label.grid(row=0, column=1, padx=20, pady=5)

    tie_score_label = ctk.CTkLabel(score_frame, text=f"Ties: {tie_score}", font=("Poppins ExtraBold", 18, "bold"),
                                   text_color="#334195")  # Orange color for ties
    tie_score_label.grid(row=0, column=2, padx=20, pady=5)

    # Images for Rock, Paper, Scissors
    rock_img = load_and_resize_image("RockT.png", 150, 150)
    rock_label = ctk.CTkLabel(app,text="Rock", font=("Poppins ExtraBold", 25), text_color="#334195")
    rock_label.place(x=250, y=240)


    paper_img = load_and_resize_image("PaperT.png", 150, 150)
    paper_label = ctk.CTkLabel(app,text="Paper", font=("Poppins ExtraBold", 25), text_color="#334195")
    paper_label.place(x=410, y=240)

    scissor_img = load_and_resize_image("ScissorT.png", 150, 150)
    scissor_label = ctk.CTkLabel(app,text="Scissor", font=("Poppins ExtraBold", 25), text_color="#334195")
    scissor_label.place(x=560, y=240)

    # Buttons for each choice
    button_frame = ctk.CTkFrame(app, fg_color="#caf0f8", corner_radius=10)
    button_frame.pack(pady=20)

    rock_button = ctk.CTkButton(button_frame, image=rock_img, fg_color="#caf0f8",text="", width=100, height=100,hover_color="#8ecae6",command=lambda: [play_game("Rock")])
    paper_button = ctk.CTkButton(button_frame, image=paper_img, fg_color="#caf0f8", text="", width=100, height=100,hover_color="#8ecae6",command=lambda: [play_game("Paper")])
    scissor_button = ctk.CTkButton(button_frame, image=scissor_img, fg_color="#caf0f8", text="", width=100, height=100,hover_color="#8ecae6",command=lambda: [play_game("Scissors")])

    rock_button.image = rock_img  # Keep reference to prevent garbage collection
    paper_button.image = paper_img
    scissor_button.image = scissor_img
    # Arrange buttons
    rock_button.grid(row=0, column=0, padx=15, pady=10)
    paper_button.grid(row=0, column=1, padx=15, pady=10)
    scissor_button.grid(row=0, column=2, padx=15, pady=10)

def play_game(player):
    global player_choice, computer_choice,player_score, computer_score,tie_score
    player_choice = player
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    animate_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    if result == "Win":
        player_score += 1
    elif result == "Lose":
        computer_score += 1
    else:
        tie_score +=1
    gg()
    player_score_label.configure(text=f"Player Score: {player_score}")
    computer_score_label.configure(text=f"Computer Score: {computer_score}")
    tie_score_label.configure(text=f"Ties: {tie_score}")

def gg():
    global result_label

    if 'result_label' in globals() and result_label is not None:
        result_label.configure(
            text=f"You chose {player_choice}\nComputer chose {computer_choice}\nYou {determine_winner(player_choice, computer_choice)}!")
    else:
        result_label = ctk.CTkLabel(app,
                                    text=f"You chose {player_choice}\nComputer chose {computer_choice}\nYou {determine_winner(player_choice, computer_choice)}!",font=("Poppins ExtraBold", 25, "bold"),
                                    text_color="#334195")

        result_label.pack(pady=40)

def animate_computer_choice():
    anim_label = ctk.CTkLabel(app, text="Computer is choosing...", font=("Poppins ExtraBold", 20), text_color="#777777")
    anim_label.place(x=400, y=500)
    app.update()

    for _ in range(5):  # Simple animation
        anim_label.configure(text=random.choice(["Rock...", "Paper...", "Scissors..."]))
        app.update()
        time.sleep(0.3)

    anim_label.destroy()
# Determine the game winner
def determine_winner(player, computer):
    if player == computer:
        return "Tie"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "Win"
    else:
        return "Lose"
home_screen()
app.mainloop()
