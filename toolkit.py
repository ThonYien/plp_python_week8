
import random


# TOOL 1: NUMBER GUESSING GAME
# This tool allows users to guess a secret number.

def guessing_game():

    secret_number = random.randint(1, 10)
    attempts = 0

    print("\n--- Number Guessing Game ---")
    print("Guess a number between 1 and 10.")

    while True:

        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")

        elif guess > secret_number:
            print("Too high! Try again.")

        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break


# TOOL 2: TO-DO LIST
# This tool allows users to add, view, and remove tasks.

def todo_list():

    tasks = []

    while True:

        print("\n--- TO-DO LIST ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Return to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":

            task = input("Enter your task: ")
            tasks.append(task)

            print(f"Task '{task}' added successfully!")

        elif choice == "2":

            if len(tasks) == 0:
                print("Your task list is empty.")

            else:
                print("\nYour Tasks:")

                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":

            if len(tasks) == 0:
                print("There are no tasks to remove.")

            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(input("Enter task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed = tasks.pop(task_number - 1)
                        print(f"Task '{removed}' removed successfully!")

                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


# TOOL 3: SIMPLE CALCULATOR
# This tool performs basic mathematical calculations.

def calculator():

    print("\n--- SIMPLE CALCULATOR ---")

    try:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

    except ValueError:
        print("Please enter valid numbers.")
        return

    print("\nChoose an operation:")
    print("+ Addition")
    print("- Subtraction")
    print("* Multiplication")
    print("/ Division")

    operation = input("Enter operation: ")

    if operation == "+":
        result = number1 + number2

    elif operation == "-":
        result = number1 - number2

    elif operation == "*":
        result = number1 * number2

    elif operation == "/":

        if number2 == 0:
            print("Cannot divide by zero.")
            return

        result = number1 / number2

    else:
        print("Invalid operation.")
        return

    print(f"Result: {result}")


# MAIN PROGRAM
# This menu runs until the user chooses Quit.

def main():

    print("\nWelcome to Thon Yien's Python Toolkit!")

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Number Guessing Game")
        print("2. To-Do List")
        print("3. Simple Calculator")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            guessing_game()

        elif choice == "2":
            todo_list()

        elif choice == "3":
            calculator()

        elif choice == "4":
            print("\nThank you for using my toolkit!")
            print("Have a great day. Keep learning Python!")
            break

        else:
            print("Sorry, that choice is not on the menu.")
            print("Please enter 1, 2, 3, or 4.")


# Start the program

if __name__ == "__main__":
    main()