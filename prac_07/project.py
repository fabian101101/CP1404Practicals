"""
Project class for managing project details.

Estimated time: 2 hours
Actual time: 3 hours
"""

import datetime


class Project:
    """Represent a Project object."""

    def __init__(self, name, start_date, priority, cost, completion_percentage):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost = float(cost)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return a string representation of a Project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority: {self.priority}, "
                f"estimate: ${self.cost:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Less than, used for sorting Projects by priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is 100% complete."""
        return self.completion_percentage == 100
