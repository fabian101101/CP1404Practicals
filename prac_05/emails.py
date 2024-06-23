"""
Emails
Estimate: 30 minutes
Actual:   35 minutes
"""


def main():
    emails_to_names = {}
    email = input("Email: ")

    while email != "":
        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation not in ("", "y"):
            name = input("Name: ").strip()

        emails_to_names[email] = name
        email = input("Email: ")

    print()
    for email, name in emails_to_names.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extracts a name from an email address."""
    parts = email.split('@')[0].split('.')
    name = ' '.join(parts).title()
    return name


main()
