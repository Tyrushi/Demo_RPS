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


# *** Main Routine goes here ***

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

  # ask user for choice and lowercase answer
  print()
  print("Round: {}".format(rounds_played + 1))
  choose = input("Choice: ").lower()
  
  
  if choose == "xxx":
    break
  
  rounds_played += 1
  
  # add one to number or rounds for continuous mode (prevents number or rounds being reached before user enters exit code)
  if mode == "continuous":
    num_rounds += 1

print("You played {} rounds.  Thank you.".format(rounds_played))




  