import random

def guess_the_number():
    print("Welcome to Guess the Number Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        # Take user input
        user_guess = input("Enter your guess: ")

        # Check if the input is a valid number
        if user_guess.isdigit():
            user_guess = int(user_guess)
            attempts += 1

            # Compare the user's guess with the number to guess
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                guessed = True
        else:
            print("Invalid input. Please enter a number.")

# Run the game
if __name__ == "__main__":
    guess_the_number()