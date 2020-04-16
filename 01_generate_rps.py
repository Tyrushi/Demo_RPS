import random

# List to hold game items
game_items = ["rock", "paper", "scissors"]

for item in range(1,20):
    # Choose an item from the list at random
    comp_choice = random.choice(game_items)

    print(comp_choice)
