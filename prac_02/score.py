"""
Module to determine score status.
"""

import random


def main():
    """Main function to run the score status program."""
    score = get_score()
    status = determine_score_status(score)
    print(f"Your score: {score} is {status}")

    # Generate a random score and print the result
    random_score = random.randint(0, 100)
    random_status = determine_score_status(random_score)
    print(f"Random score: {random_score} is {random_status}")


def get_score():
    """Prompt user for a score and return it as a float."""
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


main()
