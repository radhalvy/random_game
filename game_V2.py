import random

def input_range_1():
    try:
        num_range_1 = int(input("Enter the first number of the range: "))
        return num_range_1
    except ValueError:
        print("Invalid range.")
        return

def input_range_2():
    try:
        num_range_2 = int(input("Enter the second number of the range: "))
        return num_range_2
    except ValueError:
        print("Invalid range.")
        return

def random_number_game():
    range_1 = input_range_1()
    range_2 = input_range_2()
    user_num = ""
    ran_num = random.randrange(range_1, range_2)
    num_guesses = 0
    guess_limit = 5
    while user_num != ran_num:
        if num_guesses < guess_limit:
            try:
                user_num = int(input("Enter your guess: "))
            except ValueError:
                print("Invalid input.")
                return
            if user_num == ran_num:
                print("You win!")
                return
            else:
                if user_num < ran_num:
                    print("Higher.")
                    num_guesses += 1
                else:
                    print("Lower.")
                    num_guesses += 1
        else:
            print("You're out of guesses.")
            return

random_number_game()
