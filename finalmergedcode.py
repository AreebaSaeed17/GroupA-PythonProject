def AreebaCalculator():
    try:
        operation = input("Choose the operation that you want to perform: (+, -, /, *) ") 
        num_1= int(input("Enter the first number: "))
        num_2= int(input("Enter the second number: "))
    except ValueError:
        print("Invalid Input!! This program only works with numbers")
        return

    if operation=='+':
        result = num_1+ num_2
        print(f"{num_1} + {num_2} = {result}")
        
    elif operation=='-':
        result = num_1 - num_2
        print(f"{num_1} - {num_2} = {result}")
        
    elif operation == '/':
        if num_2 == 0: 
             print("Invalid division! Division by 0 isnt allowed!")
        else: 
            result = num_1 / num_2
            print(f"{num_1} / {num_2} = {result}")
           
    elif operation=='*':
        result = num_1 * num_2
        print(f"{num_1} * {num_2} = {result}")
    else:
        print("Invalid operation! Please choose from (+, -, /, *).")

#Calling the function to use it
AreebaCalculator()
      
            
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
