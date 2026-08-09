## linkedin https://www.linkedin.com/posts/noor-fatima-2501b240a_it-is-a-number-guessing-game-and-task-2-for-activity-7492204337545486336-wSxI?utm_source=share&utm_medium=member_desktop&rcm=ACoAAGhS9dwBbGp1DjhFPZGT0Q7ib3ko4pit5Yk

# Number Guessing Game – CLI

This project is a simple interactive number guessing game built with Python. The computer randomly selects a number between 1 and 100, and the player keeps guessing until they find the correct number.

After every guess, the game provides a hint to help the player. If the guess is too low, the game says **Too low**. If it is too high, the game says **Too high**. The game also keeps track of how many valid attempts the player has made.

## Features

* Generates a random number between 1 and 100
* Allows multiple guessing attempts
* Provides **Too high** and **Too low** hints
* Counts the number of attempts
* Handles invalid input
* Prevents guesses outside the 1–100 range
* Ends automatically when the correct number is guessed

## Requirements

You only need Python installed on your computer.

No external libraries are required. The `random` module used by the project is included with Python.

## How to Run

1. Open a terminal in the project folder.
2. Run the following command:

```bash
python guessing_game.py
```

3. Enter your guesses when prompted.
4. Continue guessing until you find the correct number.

## Example

```text
===== Number Guessing Game =====
I have selected a number between 1 and 100.
Try to guess it!

Enter your guess: 50
Too high! Try again.

Enter your guess: 25
Too low! Try again.

Enter your guess: 37
Too high! Try again.

Enter your guess: 32
Congratulations! You guessed the number.
The number was 32.
You guessed it in 4 attempts.
```

## Error Handling

The game handles invalid input without crashing.

For example:

```text
Enter your guess: hello
Invalid input. Please enter a whole number.
```

It also checks that the guess is within the allowed range:

```text
Enter your guess: 150
Please enter a number between 1 and 100.
```

## Project Structure

```text
NumberGuessingGame/
│
├── guessing_game.py
└── README.md
```

### guessing_game.py

Contains the complete game logic, including random number generation, user input, hints, attempt counting, and validation.

### README.md

Contains the project documentation and instructions for running the game.

## Technologies Used

* Python
* Command Line Interface (CLI)
* Python `random` module

## Learning Outcomes

This project provides practice with:

* Python functions
* Random number generation
* `while` loops
* Conditional statements
* User input
* Exception handling
* Input validation
* Counting attempts
* Basic game logic

## Future Improvements

Some possible improvements include:

* Adding difficulty levels
* Setting a maximum number of attempts
* Allowing the player to restart without closing the program
* Adding a score system
* Keeping track of the best score
* Adding different number ranges

## Author

Built as a Python CLI project to practice programming fundamentals, loops, conditional logic, random number generation, and user input handling.
