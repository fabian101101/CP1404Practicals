"""
Word Occurrences
Estimate: 30 minutes
Actual:   25 minutes
"""


def main():
    # Get user input
    text = input("Text: ")

    # Split the input text into words and count occurrences
    word_counts = {}
    for word in text.split():
        word_counts[word] = word_counts.get(word, 0) + 1

    # Sort the dictionary by keys (words)
    sorted_words = sorted(word_counts.keys())

    # Find the longest word for formatting purposes
    max_length = max(len(word) for word in sorted_words)

    # Print the word occurrences aligned nicely
    for word in sorted_words:
        print(f"{word:{max_length}} : {word_counts[word]}")


main()
