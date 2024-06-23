def main():
    """Read Wimbledon data, process it, and display champions and countries."""
    filename = "wimbledon.csv"
    data = read_file(filename)
    champions = count_champions(data)
    countries = extract_countries(data)
    display_champions(champions)
    display_countries(countries)


def read_file(filename):
    """Read the Wimbledon data file."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        file.readline()
        data = [line.strip().split(",") for line in file]
    return data


def count_champions(data):
    """Count how many times each champion has won."""
    champions = {}
    for entry in data:
        champion = entry[2]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def extract_countries(data):
    """Extract the unique countries from the data."""
    countries = {entry[1] for entry in data}
    return sorted(countries)


def display_champions(champions):
    """Display the champions and the number of times each has won."""
    print("Wimbledon Champions:")
    for champion, count in sorted(champions.items()):
        print(f"{champion} {count}")


def display_countries(countries):
    """Display the list of countries that have won Wimbledon in alphabetical order."""
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


main()
