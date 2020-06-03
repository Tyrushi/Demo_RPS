# RPS Component 8 - Complete Game
# v1 - Added instructions and easy to read outputs...

# To Do
# Usability Test

import random

# Functions go here


# Round checking function
def check_rounds():
    while True:
        response = input("How many rounds? ")

        round_error = "Please type either <enter> or an integer that is more than 0..."
        print()
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# User choice checking function
def check_choice(question, options):
    valid = False
    while not valid:
        response = input(question)
        response = response.lower()     # make response all lower case

        if response == "xxx":
            return response
        elif response == "r":
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


# Feedback generator
def feedback(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print


# main routine goes here...

# initialise variables
rps_list = ["rock", "paper", "scissors"]

# Instructions go here...
intro_heading ="---          Rock / Paper / Scissors - Instructions          ---"
feedback(intro_heading, "-")
print("For each game either choose the number of rounds or press <enter> for \n"
      "continuous mode.  Note that you can end a game early by pressing 'xxx'.\n"
      "\n"
      "When prompted choose Rock / Paper or Scissors\n"
      "At the end of each game, you will see a game summary.  At that point you \n"
      "can either play again (press <enter> when prompted) or quit by pressing\n"
      "any key.")
print("-" * len(intro_heading))



keep_going = ""

while keep_going == "":
    # Play game

    result = ""

    # Rounds won will be calculated (total - draw - lost)
    rounds_played = 0
    rounds_lost = 0
    rounds_drawn = 0

    end_game = "no"

    # Play Game
    print()
    rounds = check_rounds()

    while end_game == "no":
        # Generate computer choice
        comp_choice = random.choice(rps_list)


        # Get user choice

        if rounds == "":
            heading = "Continuous Mode: Round {}".format(rounds_played + 1)
            print(heading)

        else:
            heading = "Round {} of {}".format(rounds_played + 1, rounds)
            print(heading)

            if rounds_played == rounds - 1:
                end_game = "yes"

        user_choice = check_choice("Please choose rock (r), paper (p) or scissors (s): ", rps_list)

        if user_choice == "xxx":
            break

        rounds_played += 1  # This must be AFTER the break otherwise the rounds won calculation will be incorrect.


        # Compare choices
        if comp_choice == user_choice:
            result = "It's a tie"
            rounds_drawn += 1
            character = "-"
        elif user_choice == "rock" and comp_choice == "scissors":
            result = "You won!"
            character ="*"
        elif user_choice == "paper" and comp_choice == "rock":
            result = "You won!"
            character ="*"
        elif user_choice == "scissors" and comp_choice == "paper":
            result = "You won!"
            character ="*"
        else:
            result = "You lost"
            rounds_lost += 1
            character = "#"


        result_statement = "User: {}    |    Computer: {}    |    Result: {}".format(user_choice, comp_choice, result)
        print()
        # Output result
        feedback(result_statement, character)
        print()

    # End of Game Statements
    summary_statement = "Won: {}    |    Lost: {}    |   Draw: {}".format(rounds_played-rounds_drawn-rounds_lost,
                                                                          rounds_lost, rounds_drawn)
    print()
    print("*******   End Game Summary   *******")
    print(summary_statement)
    print("*" * len(summary_statement))
    print()

    keep_going = input("Press <enter> to play again or any key to quit...")
    print()

feedback("----    Thanks for playing    ----", "-")
