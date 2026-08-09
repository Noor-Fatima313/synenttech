# Simple Calculator - CLI


def calculator():
    print("===== Simple Calculator =====")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ").strip()
            num2 = float(input("Enter second number: "))

            if operator == "+":
                result = num1 + num2

            elif operator == "-":
                result = num1 - num2

            elif operator == "*":
                result = num1 * num2

            elif operator == "/":
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                    continue
                result = num1 / num2

            else:
                print("Error: Invalid operator.")
                continue

            print(f"Result: {result}")

        except ValueError:
            print("Error: Please enter valid numbers.")

        again = input("\nDo you want to calculate again? (y/n): ").strip().lower()

        if again != "y":
            print("Calculator closed.")
            break


if __name__ == "__main__":
    calculator()