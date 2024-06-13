"""
Module to handle password input and display asterisks.
"""

MIN_LENGTH = 8


def main():
    """Main function to run the password program."""
    password = get_valid_password(MIN_LENGTH)
    print_asterisks(password)


def get_valid_password(min_length):
    """Prompt user for a password and ensure it meets the minimum length requirement."""
    password = input(f"Enter password (minimum {min_length} characters): ")
    while len(password) < min_length:
        print(f"Invalid password! Password must be at least {min_length} characters long.")
        password = input(f"Enter password (minimum {min_length} characters): ")
    return password


def print_asterisks(password):
    """Print asterisks equal to the length of the password."""
    print('*' * len(password))


main()
