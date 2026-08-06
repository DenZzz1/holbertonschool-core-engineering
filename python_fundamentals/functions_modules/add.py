#!/usr/bin/env python3
"""Module that imports the add function and prints 1 + 2 = 3."""
from add_0 import add


if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
