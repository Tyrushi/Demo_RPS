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

#  *** Main Routine starts here ***

# Set up list for user choice AND computer choice
rps = ["rock", "paper", "scissors"]

# Get user choice...
user_choice = string_checker("Choose: ", rps)
print(user_choice)

comp_choice = random.choice(rps)
print(comp_choice)




# **** Main Routine goes here ****