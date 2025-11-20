import random

def guessing_game_fatima():
    print(" Welcome to Fatima's Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")

    while True:
        number_to_guess = random.randint(1, 50)
        attempts = 0

        while True:
            try:
                guess = int(input("Enter your guess (1–50): "))
                attempts += 1

                if guess < 1 or guess > 50:
                    print("Please guess a number between 1 and 50.")
                elif guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f" Correct! You guessed it in {attempts} attempts.")
                    break
            except ValueError:
                print(" Invalid input! Please enter a number.")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! byee")
            break
