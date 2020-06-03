import random

# **** Functions go here... ****

# Checks user input (either full word or first letter of word)
def string_checker(question, to_check):
  
  valid = False
  while not valid:
    # ask user question and change response to lowercase
    response = input(question).lower()

    # check response is in list OR that it's the first letter of an item in the list
    for item in to_check:
      if response == item:
        return response
      elif response == item[0]:
        return item

    # if item not in list, print error
    print("sorry that is not a valid response")


# Compare user choice and computer choice
def rps_compare(rps_list, user, comp):

  # Compare options...

  # If they're the same, it's a tie
  if user == comp:
    result = "It's a tie!"

  # Three ways to win
  elif user == "rock" and comp == "scissors":
    result = "You won!"
  elif user == "paper" and comp == "rock":
    result = "You won!"
  elif user == "scissors" and comp == "paper":
    result = "You won!"

  # If one does not win / tie, it's a loss
  else:
    result = "You lost"

  return result




#  *** Main Routine starts here ***

# Set up list for user choice AND computer choice
rps = ["rock", "paper", "scissors"]

# Get user choice...
user_choice = string_checker("Choose: ", rps)
print(user_choice)

comp_choice = random.choice(rps)
print(comp_choice)

compare = rps_compare(rps, user_choice, comp_choice)
print(compare)

# Compare user and computer choice



# **** Main Routine goes here ****