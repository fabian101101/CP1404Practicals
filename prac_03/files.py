"""
CP1404/CP5632 - Practical
Writing and reading files using different techniques.
"""

# Question 1
name = input("Enter your name: ")
name_file = open("name.txt", "w")
name_file.write(name)
name_file.close()

# Question 2
name_file = open("name.txt", "r")
name = name_file.read().strip()
name_file.close()
print(f"Hi {name}!")

# Question 3
with open("numbers.txt", "r") as numbers_file:
    first_number = int(numbers_file.readline().strip())
    second_number = int(numbers_file.readline().strip())
    result = first_number + second_number
print(result)

# Question 4
total = 0
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        total += int(line.strip())
print(total)
