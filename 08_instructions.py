def instructions():

  first_time = input("Would you like to read the instructions? ")

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

# **** Main routine *****
instructions()
