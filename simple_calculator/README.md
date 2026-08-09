# Simple Calculator – CLI
## linkedin https://www.linkedin.com/posts/noor-fatima-2501b240a_task1-for-python-programming-at-synent-technologies-activity-7492201119356616705-Hlk2?utm_source=share&utm_medium=member_desktop&rcm=ACoAAGhS9dwBbGp1DjhFPZGT0Q7ib3ko4pit5Yk

This project is a simple command-line calculator built with Python. It allows the user to perform basic mathematical operations directly in the terminal without needing a graphical interface.

The calculator supports addition, subtraction, multiplication, and division. It also includes basic error handling so that invalid numbers, unsupported operators, and division by zero do not crash the program.

## Features

* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`*`)
* Division (`/`)
* Takes numbers and operators from the user
* Handles invalid number inputs
* Handles invalid operators
* Prevents division by zero
* Allows the user to perform multiple calculations
* Runs entirely in the terminal

## Requirements

You only need Python installed on your computer.

No external Python libraries are required.

## How to Run

1. Download or clone the project.
2. Open a terminal in the project folder.
3. Run the following command:

```bash
python calculator.py
```

## Example

```text
===== Simple Calculator =====
Enter first number: 25
Enter operator (+, -, *, /): +
Enter second number: 15
Result: 40.0

Do you want to calculate again? (y/n): y

Enter first number: 20
Enter operator (+, -, *, /): /
Enter second number: 5
Result: 4.0
```

## Error Handling

The calculator checks for invalid input.

For example, if the user enters text instead of a number:

```text
Enter first number: hello
Error: Please enter valid numbers.
```

It also prevents division by zero:

```text
Enter first number: 10
Enter operator (+, -, *, /): /
Enter second number: 0
Error: Cannot divide by zero.
```

If an unsupported operator is entered:

```text
Enter operator (+, -, *, /): %
Error: Invalid operator.
```

## Project Structure

```text
SimpleCalculator/
│
├── calculator.py
└── README.md
```

### calculator.py

Contains the complete calculator program, including user input, mathematical operations, validation, and error handling.

### README.md

Contains the project documentation and instructions for running the calculator.

## Technologies Used

* Python
* Command Line Interface (CLI)

## Learning Outcomes

This project helped practice:

* Python functions
* User input
* Conditional statements
* Exception handling
* Loops
* Basic arithmetic operations
* Input validation

## Future Improvements

Possible improvements include:

* Adding percentage calculations
* Adding power and square-root operations
* Adding calculation history
* Creating a graphical user interface
* Supporting more advanced mathematical operations

## Author

Built as a Python CLI project to practice the fundamentals of programming and user input handling.
