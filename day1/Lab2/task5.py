import random


def play_game(tries=10):
    random_num = random.randint(1, 100)
    guessed_nums = set()

    while tries > 0:
        user_num = input(
            f"Guess the number (1-100). You have {tries} tries left: ")

        # Check if user input is out of range
        if not user_num.isdigit() or int(user_num) < 1 or int(user_num) > 100:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue

        user_num = int(user_num)

        # Check if user has already guessed the number
        if user_num in guessed_nums:
            print("You already guessed that number. Try again.")
            continue

        guessed_nums.add(user_num)

        if user_num == random_num:
            print("Congratulations! You guessed the number!")
            print("You have {} tries left. Guess a new number!".format(
                tries))

            play_again = input("Do you want to play again? (y/n): ")

            if play_again.lower() == "y":
                play_game(tries)
            else:
                print("Thanks for playing!")
            return

        if user_num < random_num:
            print("Your guess is Low..")
        else:
            print("Your guess is high..")

        tries -= 1

    print(f"Sorry, you lost. The number was {random_num}.")
    play_again = input("Do you want to play again? (y/n): ")

    if play_again.lower() == "y":
        play_game()
    else:
        print("Thanks for playing!")


play_game()
