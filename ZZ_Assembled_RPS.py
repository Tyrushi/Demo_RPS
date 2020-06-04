import random

# **** Functions go here... ****
def instructions():

  first_time = string_checker("Would you like to read the instructions? ", ["yes", "no"])

  if first_time == "no":
    return ""
  
  else:
    print()
    print("******* RPS Instructions ********")
    print()
    print("Either choose a number or rounds or \n press enter to play continuous mode.  Note that you can type 'xxx' as a choice at any time to quite the game and view your summary statistics.")
    print()
    print("The rules are simple...")
    print("Rock beats scissors")
    print("Scissors beats paper")
    print("Paper beats rock")
    print()
    print("Have fun!")
    print()


def statement_generator(statement, char):
  print(len(statement) * char)
  print(statement)
  print(len(statement) * char)
  return ""

# Gets number or rounds / continuous mode
def get_rounds():

  error = "Please enter an integer that is more than 0 or press <enter>"

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
    result = "tie"

  # Three ways to win
  elif user == "rock" and comp == "scissors":
    result = "win"
  elif user == "paper" and comp == "rock":
    result = "win"
  elif user == "scissors" and comp == "paper":
    result = "win"

  # If one does not win / tie, it's a loss
  else:
    result = "lose"

  return result




#  *** Main Routine starts here ***

statement_generator("***Welcome to the Great RPS Game ***", "*")

print()

# Ask user if they have played game before and display instructions if desired.
instructions()


# Set up lists
rps = ["rock", "paper", "scissors"]   # choices for user and computer
game_summary = [] # Holds results from each round

# Initialise counters
rounds_played = 0
win = 0
lose = 0
tie = 0

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
  print("Round #{}".format(rounds_played + 1))

  # Get user choice...
  user_choice = string_checker("Choose: ", rps)
  
  if user_choice.lower() == "xxx":
    break
  
  rounds_played += 1
  
  # add one to number or rounds for continuous mode (prevents number or rounds being reached before user enters exit code)
  if mode == "continuous":
    num_rounds += 1

  # Get Computer Choice
  comp_choice = random.choice(rps)

  # Compare user and computer choice
  compare = rps_compare(rps, user_choice, comp_choice)

  if compare == "win":
    win += 1
    decoration = "*"
  elif compare == "lose":
    lose += 1
    decoration = "!"
  else:
    tie += 1
    decoration = "="

  result = "{} vs {} : {}".format(user_choice, comp_choice, compare)

  # Output result to user
  print()
  statement_generator(result, decoration)
  print()

  # add result to game summary (to be ouput at end)
  game_summary.append("Round #{} - {}".format(rounds_played,result))


# Calculate Game statistics
percent_win = win / rounds_played * 100
percent_lose = lose / rounds_played * 100
percent_tie = tie / rounds_played * 100

# End of game, Print Stats
print()
print("**** Game History ****")
for item in game_summary:
  print(item)

print()

print("******* Game Statistics ********")
print("Win: {}, ({:.0f}%)\nLoss: {}, ({:.0f}%)\nTie: {}, ({:.0f}%)".format(win, percent_win, lose, percent_lose, tie, percent_tie))
print()

print("Thanks for playing.")



