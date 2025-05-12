# autoDocstring taper 3 fois " pour avoir l'autoDoc

import typing as t 
from typing import List, Dict, Union


def square(x: int = 3) -> int:
    """
    Calcule le carré d'un nombre entier donné.

    Parameters
    ----------
    x : int, optional
        Le nombre entier à élever au carré, par défaut 3.

    Returns
    -------
    int
        Le carré de l'entier fourni.
    """
    return x ** 2


def triple_letter(letter: str) -> t.List[str]:
    """
    Crée une liste contenant trois fois une lettre donnée.

    Parameters
    ----------
    letter : str
        La lettre à répéter dans la liste.

    Returns
    -------
    t.List[str]
        Une liste de chaînes de caractères contenant trois fois la lettre fournie.
    """
    return [letter] * 3

def find_max(numbers: List[int]) -> int:
    """
    Finds the maximum integer in a list of integers.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        int: The maximum integer in the list.
    """
    if not numbers:
        raise ValueError("The list is empty.")
    return max(numbers)

def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Divides two numbers, returning an integer if both inputs are integers, otherwise a float.

    Args:
        a (Union[int, float]): The numerator.
        b (Union[int, float]): The denominator.

    Returns:
        Union[int, float]: The result of the division.

    Raises:
        ZeroDivisionError: If the denominator is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b if isinstance(a, float) or isinstance(b, float) else a // b


def add_entry(d: Dict[str, int], key: str, value: int) -> Dict[str, int]:
    """
    Adds a new key-value pair to the dictionary.

    Args:
        d (Dict[str, int]): The dictionary to which the entry will be added.
        key (str): The key for the new entry.
        value (int): The value associated with the key.

    Returns:
        Dict[str, int]: The dictionary with the new key-value pair added.
    """
    d[key] = value
    return d



def main() -> None:
    """
    Exécute la fonction principale du script.

    Cette fonction initialise un entier, appelle la fonction `result` avec cet entier, 
    puis imprime le résultat qui est le carré de cet entier.

    Returns
    -------
    None
        Cette fonction ne retourne rien. Elle affiche simplement le résultat.
    """
    n = 3
    print(square(n))


if __name__ == "__main__":
    main()

#Dans le terminal, entrer dans le fichier qui contient ce code 
# Puis python mon_fichier.py
