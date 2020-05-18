import random


def game():
    # generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    guesses = []
    while len(guesses) < 5:
        try:
            # get a number from the player
            user_guess = int(input("Enter a number between 1 and 10 "))
        except ValueError:
            print("That's not a number!")
        else:
            # compare guess to secret number
            if user_guess == secret_number:
                print("Well done! You guess it")
                break
            elif user_guess > secret_number:
                print("Too High...")
            elif user_guess < secret_number:
                print("Too Low...")
            else:
                print("You miss :-(")
            guesses.append(user_guess)
    else:
        print(f"You didn't get it! My number was {secret_number}")

    play_again = input('Do want to play again? Y/N ')
    if play_again.lower() != 'n':
        game()
    else:
        print("Bye!!")


game()
