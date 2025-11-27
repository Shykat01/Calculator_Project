"""
Python Calculator Project
By: Sazzadul Islam Shykat
Phn:01616498901
"""


# Basic Arethmetic Functions

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def multiply(a, b):
    return a*b

def div(a, b):
    return a/b


#Input Validition Function

def get_valid_number(prompt = "Enter a number: "):
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)
            return number
        except ValueError:
            print(f"Invalid input: '{user_input}' is not a valid number. Please try again.")

#Display Result Function

def display(num1, num2):
    print(f"\nResult for {num1} and {num2}: ")
    print("-" * 30)
    print(f"Addition:       {num1} + {num2} = {add(num1, num2)}")
    print(f"Subtraction:    {num1} - {num2} = {sub(num1, num2)}")
    print(f"Multiplication: {num1} × {num2} = {multiply(num1, num2)}")

    div_result = div(num1 , num2)
    if div_result is None:
        print(f"Division:       {num1} ÷ {num2} = Error (cannot divide by zero)")
    else:
        print(f"Division:       {num1} ÷ {num2} = {div_result}")
    print("-" * 30)


#Calculator Menu

def show_menu():
    print("\n" + "=" * 35)
    print("       PYTHON CALCULATOR")
    print("=" * 35)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("=" * 35)


def run_calculator():
    print("\nWelcome to the Mini Calculator!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '5':
            print("\nThank you for using the calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("\nInvalid choice. Please enter a number between 1 and 5.")
            continue


        num1 = get_valid_number("Enter first number: ")
        num2 = get_valid_number("Enter second number: ")


        if choice == '1':
            result = add(num1, num2)
            print(f"\n{num1} + {num2} = {result}")

        elif choice == '2':
            result = sub(num1, num2)
            print(f"\n{num1} - {num2} = {result}")

        elif choice == '3':
            result = multiply(num1, num2)
            print(f"\n{num1} × {num2} = {result}")

        elif choice == '4':
            result = div(num1, num2)
            if result is None:
                print(f"\n{num1} ÷ {num2} = Error: Cannot divide by zero!")
            else:
                print(f"\n{num1} ÷ {num2} = {result}")


#OOP Calculator Class

class Calculator:
    def __init__(self):
        self.history = []


    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return  "Error : Cannot divide by Zero!"
        return  a / b

    def get_valid_number(self, prompt="Enter a number: "):
        while True:
            try:
                user_input = input(prompt)
                number = float(user_input)
                return number
            except ValueError:
                print(f"Invalid input: '{user_input}' is not a valid number. Please try again.")

    def menu(self):

        print("\n" + "=" * 40)
        print("      OOP MINI CALCULATOR By Shykat")
        print("=" * 40)
        print("  1. Add")
        print("  2. Subtract")
        print("  3. Multiply")
        print("  4. Divide")
        print("  5. Exit")
        print("  6. View History")
        print("=" * 40)

    def show_history(self):
        print("\n" + "=" * 35)
        print("         Calculation History")
        print("=" * 35)

        if not self.history:
            print("No history found!")
        else:
            for i, record in enumerate(self.history, 1):
                print(f"{i}. {record}")

        print("=" * 35)


    def run(self):
        print("\n" + "*" * 40)
        print("  Welcome to the OOP MINI Calculator!")
        print("*" * 40)

        while True:

            self.menu()

            choice = input("Enter your choice (1-5): ").strip()

            if choice == '5':
                print("\n" + "-" * 40)
                print("Thank you for using the Calculator!")
                print("Goodbye!")
                print("-" * 40)
                break

            if choice == '6':
                self.show_history()
                continue

            if choice not in ['1', '2', '3', '4']:
                print("\n⚠ Invalid choice! Please enter a number between 1 and 5.")
                continue

            print()
            num1 = self.get_valid_number("Enter first number: ")
            num2 = self.get_valid_number("Enter second number: ")

            print("\n" + "-" * 30)

            if choice == '1':
                result = self.add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
                self.history.append(f"{num1} + {num2} = {result}")

            elif choice == '2':
                result = self.sub(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
                self.history.append(f"{num1} - {num2} = {result}")

            elif choice == '3':
                result = self.multiply(num1, num2)
                print(f"Result: {num1} × {num2} = {result}")
                self.history.append(f"{num1} × {num2} = {result}")

            elif choice == '4':
                result = self.div(num1, num2)
                if isinstance(result, str):  # Error message for division by zero
                    print(f"Result: {num1} ÷ {num2} = {result}")
                else:
                    print(f"Result: {num1} ÷ {num2} = {result}")
                    self.history.append(f"{num1} ÷ {num2} = {result}")

            print("-" * 30)


#Main Program

if __name__ == "__main__":
    calc = Calculator()
    calc.run()




