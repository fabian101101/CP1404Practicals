"""
CP1404/CP5632 Practical
List exercises
"""


def main():
    # Woefully inadequate security checker
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username = input("Enter your username: ")
    if username in usernames:
        print("Access granted")
        get_numbers_and_display_info()
    else:
        print("Access denied")


def get_numbers_and_display_info():
    numbers = []

    # Prompt the user for 5 numbers and store them in the list
    for i in range(5):
        number = float(input("Number: "))
        numbers.append(number)

    # Output information about the numbers
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


main()
