"""
Hexadecimal colour lookup program.
"""

# Constant dictionary of color names and their hexadecimal codes
HEX_COLOURS = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}


def main():
    # Print the dictionary for reference (optional)
    print(HEX_COLOURS)

    # Get user input and look up color codes until a blank input is received
    colour_name = input("Enter colour name: ").strip().capitalize()
    while colour_name != "":
        try:
            print(f"{colour_name} is {HEX_COLOURS[colour_name]}")
        except KeyError:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").strip().capitalize()

    # Optionally, print all colour names and codes
    print("\nAll colour names and codes:")
    for name, code in HEX_COLOURS.items():
        print(f"{name:15} is {code}")


main()
