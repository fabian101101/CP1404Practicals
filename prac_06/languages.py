from programming_language import ProgrammingLanguage


def main():
    """Test the ProgrammingLanguage class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print the programming language objects
    print(python)
    print(ruby)
    print(visual_basic)

    # Create a list of programming languages
    languages = [python, ruby, visual_basic]

    # Print the names of dynamically typed languages
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
