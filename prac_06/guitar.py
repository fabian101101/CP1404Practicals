class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar in years."""
        return 2022 - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, False otherwise."""
        return self.get_age() >= 50
