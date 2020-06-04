import random

# **** Functions go here... ****

# Gets number or rounds / continuous mode
def get_rounds():

  error = "Please enter an integer or press <enter>"

  valid = False

  while not valid:
    print()
    response = input("How many rounds? \nPress <enter> for continuous mode: \n")

    if response == "":
      return("continuous")

    try:
      response = int(response)

      if response > 0:
        return response
      else:
        print(error)

    except ValueError:
      print(error)


# Checks user input (either full word or first letter of word)
def string_checker(question, to_check):
  
  valid = False
  while not valid:
    # ask user question and change response to lowercase
    response = input(question).lower()

    if response == "xxx":
      return response

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

rounds_played = 0

mode = get_rounds()

if mode != "continuous":
  num_rounds = mode
else: 
  num_rounds = 3

choose = ""
while choose != "xxx":

  # check there are still rounds to be played...
  if rounds_played >= num_rounds:
    break

  print()
  print("Round: {}".format(rounds_played + 1))

  # Get user choice...
  user_choice = string_checker("Choose: ", rps)
  
  if user_choice == "xxx":
    break
  
  rounds_played += 1
  
  # add one to number or rounds for continuous mode (prevents number or rounds being reached before user enters exit code)
  if mode == "continuous":
    num_rounds += 1

  # Get Computer Choice
  comp_choice = random.choice(rps)
  print(comp_choice)

  # Compare user and computer choice
  compare = rps_compare(rps, user_choice, comp_choice)
  print(compare)

# End of game, farewell message
print()
print("You played {} rounds.  Thank you.".format(rounds_played))

