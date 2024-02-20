#!/usr/bin/python3
"""
Defines a function to print text with 2 new lines
    after each occurrence of . ? and :
Attributes:
    text_indentation: function that prints a text
                        with specific conditions
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after . ? and : characters.

    Args:
        text (str): The input text to be examined.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiter in ".:?":
        text = (delimiter + "\n\n").join(
                [line.strip() for line in text.split(delimiter)])

    print(text, end="")
