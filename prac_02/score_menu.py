"""
Module to provide a score menu with various options.
"""

import random


def main():
    """Main function to run the score menu program."""
    score = None
    while True:
        display_menu()
        choice = input("Choose an option: ").upper()
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            if score is not None:
                print_result(score)
            else:
                print("You need to get a valid score first.")
        elif choice == 'S':
            if score is not None:
                show_stars(score)
            else:
                print("You need to get a valid score first.")
        elif choice == 'Q':
            print("Farewell!")
            break
        else:
            print("Invalid option, please choose again.")


def display_menu():
    """Display the score menu options."""
    print("Menu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    """Prompt user for a valid score between 0 and 100 and return it as a float."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score! Please enter a score between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


def determine_score_status(score):
    """Determine the status of the score and return it as a string."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_result(score):
    """Print the result of the score."""
    result = determine_score_status(score)
    print(f"Your score: {score} is {result}")


def show_stars(score):
    """Display asterisks equal to the score."""
    print('*' * int(score))


main()
