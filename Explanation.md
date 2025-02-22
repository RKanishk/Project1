# Code Explanation

## Importing necessary modules
The `random` module is imported to generate a random number.

```python
import random
```

## Defining the main function
The main function `guess_the_number` is defined to encapsulate the game logic.

```python
def guess_the_number():
    # Function code here
```

## Generating a random number
A random number between 1 and 100 is generated using `random.randint`.

```python
number_to_guess = random.randint(1, 100)
```

## Taking user input
The user is prompted to enter their guess. The input is checked to ensure it is a valid number.

```python
user_guess = input("Enter your guess: ")

if user_guess.isdigit():
    user_guess = int(user_guess)
```

## Checking the user's guess
The user's guess is compared with the generated number. Feedback is provided based on whether the guess is too low, too high, or correct.

```python
if user_guess < number_to_guess:
    print("Too low! Try again.")
elif user_guess > number_to_guess:
    print("Too high! Try again.")
else:
    print(f"Congratulations! You guessed the number in {attempts} attempts.")
    guessed = True
```

## Looping until the correct number is guessed
A loop is used to keep prompting the user for a guess until the correct number is guessed.

```python
while not guessed:
    # Loop code here
```
