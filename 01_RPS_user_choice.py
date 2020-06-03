# RPS Component 2 - Ask user for their choice

def check_choice(question, options):
    valid = False
    while not valid:
        response = input(question)
        response = response.lower()     # make response all lower case

        if response == "r":
            response = "rock"
        elif response == "p":
            response = "paper"
        elif response == "s":
            response = "scissors"

        if response in options:
            return response
        else:
            print("I don't understand...")
            print()

# main routine goes here...
rps_list = ["rock", "paper", "scissors"]

for item in range(0,6):     # run 6 times so I can test multiple options
    user_choice = check_choice("Please choose rock (r), paper (p) or scissors (s): ", rps_list)
    print("You chose {}".format(user_choice))
