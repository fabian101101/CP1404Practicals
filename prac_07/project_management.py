"""
Project Management Program.

Estimated time: 4 hours
Actual time: 6 hours
"""

import datetime
from project import Project

MENU = """
- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
"""


def main():
    """Main function to manage the Project Management Program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")

    while True:
        print(MENU)
        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            if input("Would you like to save to projects.txt? (y/n): ").lower() == 'y':
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice")


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()
        for line in file:
            parts = line.strip().split('\t')
            projects.append(Project(*parts))
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.cost}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display incomplete and completed projects."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(f"  {project}")
    print("Completed projects:")
    for project in sorted(completed_projects):
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter projects by start date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > date]

    print("Filtered projects:")
    for project in sorted(filtered_projects, key=lambda x: x.start_date):
        print(f"  {project}")


def add_new_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: "))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost, completion_percentage))


def update_project(projects):
    """Update a project's completion percentage and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_index = int(input("Project choice: "))
    project = projects[project_index]
    print(project)

    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")

    if new_percentage:
        project.completion_percentage = int(new_percentage)
    if new_priority:
        project.priority = int(new_priority)


if __name__ == '__main__':
    main()
