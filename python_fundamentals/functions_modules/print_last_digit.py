#!/usr/bin/env python3
"""Module that defines a function to print the last digit of a number."""


def print_last_digit(number):
    """Print and return the last digit of number (always positive)."""
    last_digit = abs(number) % 10
    print("{}".format(last_digit))
    return last_digit
