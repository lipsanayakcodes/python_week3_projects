#Calculator Class with Exception Handling
class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


# Create calculator object
calculator = Calculator()

while True:

    print("\n===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Thank you for using Calculator!")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = calculator.add(num1, num2)
            print("Result:", result)

        elif choice == "2":
            result = calculator.subtract(num1, num2)
            print("Result:", result)

        elif choice == "3":
            result = calculator.multiply(num1, num2)
            print("Result:", result)

        elif choice == "4":
            result = calculator.divide(num1, num2)
            print("Result:", result)

        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    except ZeroDivisionError as error:
        print("Error:", error)