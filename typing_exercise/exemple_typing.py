# autoDocstring taper 3 fois " pour avoir l'autoDoc

import typing as t 
from typing import List, Dict, Union


def square(x):
    return x ** 2


def triple_letter(letter):
    return [letter] * 3

def find_max(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    return max(numbers)

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b if isinstance(a, float) or isinstance(b, float) else a // b


def add_entry(d, key, value):
    d[key] = value
    return d



def main():
    n = 3
    print(square(n))


if __name__ == "__main__":
    main()

#Dans le terminal, entrer dans le fichier qui contient ce code 
# Puis python mon_fichier.py

