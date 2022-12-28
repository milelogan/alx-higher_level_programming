#!/usr/bin/python3
""" a function that prints My name is <first name> <last name> """


def say_my_name(first_name, last_name=""):
    """
    Prints my name is <first name> <last name>

    Args:
            first_name: first name
            last_name: the surname
    Returns:
            first_name must be a string or last_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
