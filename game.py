import random

def random_number_game():
    user_num = ""                       # Variable declaration
    ran_num = random.randrange(0, 101)  # Random number stored and range of that number
    num_guesses = 0                     # Number of the current amount of guesses of the player
    guess_limit = 5                     # Limit of the tries that the player has
    while user_num != ran_num:          # Loop to continue with the game even if the answer is wrong
        if num_guesses < guess_limit:   # Confirmation to see if the player has any guesses left
            try:
                user_num = int(input("Enter your guess: "))     # Guess of the player
            except ValueError:                                  # Except just in case the player enters a string or a float and not a number
                print("Invalid input.")
                return
            if user_num == ran_num:     # Confirmation to see if the player answered correctly
                print("You win!")
                return
            else:
                if user_num < ran_num:  # Checking if the number entered by the player is higher than the number created randomly
                    print("Higher.")
                    num_guesses += 1    # Avoiding an infinite loop
                else:                   # Checking if the number entered by the player is lower than the number created randomly
                    print("Lower.")
                    num_guesses += 1    # Avoiding an infinite loop
        else:                           # Case in which the player has no more tries
            print("You're out of guesses.")
            return

random_number_game()
