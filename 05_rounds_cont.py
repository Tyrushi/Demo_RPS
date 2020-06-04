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

num_rounds = get_rounds()
print(num_rounds)