import csv
from guitar import Guitar


def main():
    """Read guitar data from a file, store them in a list, and display them."""
    guitars = load_guitars("guitars.csv")
    print("These are the guitars:")
    for guitar in guitars:
        print(guitar)

    guitars.sort()
    print("\nThese are the guitars sorted by year:")
    for guitar in guitars:
        print(guitar)

    add_guitars(guitars)
    save_guitars("guitars.csv", guitars)


def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def save_guitars(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def add_guitars(guitars):
    """Add new guitars from user input."""
    print("\nAdd new guitars (leave name blank to stop):")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $ "))
        guitars.append(Guitar(name, year, cost))


if __name__ == '__main__':
    main()
