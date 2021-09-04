import random
import math


def get_first_range():
    num_range_1 = int(input("\nEnter the first number of the range: "))
    return num_range_1


def get_second_range():
    num_range_2 = int(input("\nEnter the second number of the range: "))
    return num_range_2


def get_user_guess():
    user_guess = int(input("\nEnter your guess: "))
    return user_guess


def get_math_log(number):
    log = math.log(number)
    return log


def main():
    try:
        first_range = get_first_range()
        second_range = get_second_range()
    except ValueError:
        print("\nInvalid range.")
    else:
        first_range_log = get_math_log(first_range)
        second_range_log = get_math_log(second_range)
        random_number = random.randrange(first_range, second_range)
        num_guesses = 0
        # It's gonna take the 2 numbers that the user inputs for the range and it's gonna calculate them to set the limit of guesses
        guess_limit = round(second_range_log - first_range_log + 1)
        print(f"\nYou have {guess_limit} tries to guess the number!")
        user_guess = ""
        while user_guess != random_number:
            if num_guesses < guess_limit:
                try:
                    user_guess = get_user_guess()
                except ValueError:
                    print("\nInvalid input.")
                    return
                else:
                    if user_guess == random_number:
                        print("\nYou win!")
                        return
                    else:
                        if user_guess < random_number:
                            print("\nHigher.")
                            num_guesses += 1
                        else:
                            print("\nLower.")
                            num_guesses += 1
            else:
                print("\nYou're out of guesses.")
                return


main()
