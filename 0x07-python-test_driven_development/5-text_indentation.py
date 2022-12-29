#!/usr/bin/python3

""" a function that prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """
    A function that prints a text with 2 lines after each of the special characters

    Args:
            text: the string

    Returns:
            TypeError: text must be a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    while count < len(text) and text[count] == " ":
        count = count + 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count = count + 1
            while count < len(text) and text[count] == " ":
                count = count + 1
            continue
        count = count + 1
