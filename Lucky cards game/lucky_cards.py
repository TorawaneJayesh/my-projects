# # here i have create a game that name is lucky cards

# import random

# p1 = input("enter player one name:")
# p2 = input("enter player two name:")
# p3 = input("enter player three name:")
# p4 = input("enter player four name:")

# cards = [0,5,7,10]
# players = [p1,p2,p3,p4]

# enumerate(cards,start=1)
# enumerate(players,start=1)

# while True:
#     choice = input("enter to start game and 'exit' for exit:")
#     if choice == 'exit':
#         print("you are exit the game!")
#         break
#     else:
#         random.shuffle(cards)
#         random.shuffle(players)
#         for i in range(1,5):
#             print(players[i-1])
#             user_cards = int(input("choose your card (1-4):"))
#             print(players[i-1],"you choose card:",cards[i-1])



import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Function to handle card selection
def choose_card(card_index):
    global current_player
    player = players[current_player]
    if card_index in chosen_cards:
        messagebox.showwarning("Invalid Choice", "This card has already been chosen.")
    else:
        chosen_cards.add(card_index)
        card = deck[card_index]
        scores[player] += card['value']
        card_buttons[card_index].config(
            image=card['image'], state="disabled"
        )  # Flip to card image
        current_player += 1
        if current_player < len(players):
            update_prompt()
        else:
            update_scores_table()
            show_controls()
            messagebox.showinfo(
                "Round Over", "This round is over. Check the scores above."
            )
            current_player = 0

# Function to start the game
def start_game():
    global chosen_cards, scores, current_player, deck
    players[:] = [entry.get() for entry in player_entries]
    if any(not player for player in players):
        messagebox.showwarning("Input Error", "Please enter names for all players.")
        return
    # Initialize deck
    deck = [{'value': value, 'image': image} for value, image in zip(cards_values, cards_images)]
    random.shuffle(deck)
    random.shuffle(players)
    chosen_cards = set()
    scores = {player: 0 for player in players}
    current_player = 0
    update_prompt()
    update_scores_table()
    entry_frame.pack_forget()
    prompt_frame.pack()
    control_frame.pack_forget()
    reset_card_buttons()  # Ensure all cards are blank initially
    score_frame.pack()  # Display the score table

# Function to update the game prompt
def update_prompt():
    prompt_label.config(text=f"{players[current_player]}, choose your card:")

# Function to update the scores table
def update_scores_table():
    for i, player in enumerate(players):
        score_labels[i].config(text=f"{player}: {scores[player]} points")

# Function to show the final results
def show_results():
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    results = ""
    rankings = ["Winner", "Second", "Third", "Loser"]
    for rank, (player, score) in zip(rankings, sorted_scores):
        results += f"{rank}: {player} with {score} points\n"
    messagebox.showinfo("Game Over", f"Final Rankings:\n\n{results}")
    root.quit()

# Function to retry the game
def retry_game():
    global chosen_cards, current_player, deck
    chosen_cards = set()  # Reset chosen cards
    current_player = 0
    # Reshuffle the deck
    deck = [{'value': value, 'image': image} for value, image in zip(cards_values, cards_images)]
    random.shuffle(deck)
    reset_card_buttons()  # Reset card images to blank
    prompt_frame.pack()
    control_frame.pack_forget()
    update_prompt()
    update_scores_table()

# Function to reset card buttons to blank images
def reset_card_buttons():
    for button in card_buttons:
        button.config(image=blank_image, state="normal")

# Function to exit the game
def exit_game():
    root.withdraw()  # Hide the main window
    show_results()

# Function to show control buttons
def show_controls():
    control_frame.pack()

# Initialize GUI
root = tk.Tk()
root.title("Lucky Cards Game")

# Card values and images
cards_values = [0, 5, 7, 10]  # Values of the cards

# Load card images
blank_image = ImageTk.PhotoImage(
    Image.open("card_blank.png").resize((100, 150))
)

# Load images corresponding to the card values
image_files = ["card_0.jpeg", "card_1.jpeg", "card_2.jpeg", "card_3.jpeg"]
cards_images = [
    ImageTk.PhotoImage(Image.open(img_file).resize((100, 150)))
    for img_file in image_files
]

# Initialize deck
deck = [{'value': value, 'image': image} for value, image in zip(cards_values, cards_images)]

players = []
chosen_cards = set()
scores = {}
current_player = 0

# Create GUI elements for player name entry
entry_frame = tk.Frame(root)
player_entries = [tk.Entry(entry_frame) for _ in range(4)]
for i, entry in enumerate(player_entries):
    tk.Label(entry_frame, text=f"Enter player {i+1} name:").grid(row=i, column=0)
    entry.grid(row=i, column=1)
tk.Button(entry_frame, text="Start Game", command=start_game).grid(
    row=4, column=0, columnspan=2
)

# Create GUI elements for game
prompt_frame = tk.Frame(root)
prompt_label = tk.Label(prompt_frame, text="")
prompt_label.pack(pady=10)

button_frame = tk.Frame(prompt_frame)
button_frame.pack(pady=10)
card_buttons = []
for i in range(4):
    card_button = tk.Button(
        button_frame, image=blank_image, command=lambda i=i: choose_card(i)
    )
    card_button.grid(row=0, column=i, padx=5)
    card_buttons.append(card_button)

# Create score table
score_frame = tk.Frame(root)
score_labels = [tk.Label(score_frame, text="") for _ in range(4)]
for label in score_labels:
    label.pack()

# Create control buttons
control_frame = tk.Frame(root)
start_button = tk.Button(control_frame, text="Retry", command=retry_game)
exit_button = tk.Button(control_frame, text="Exit", command=exit_game)
start_button.grid(row=0, column=0, padx=5, pady=10)
exit_button.grid(row=0, column=1, padx=5, pady=10)

# Pack frames
entry_frame.pack()

# Start the GUI event loop
root.mainloop()
