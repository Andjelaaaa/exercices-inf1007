#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number *= -1
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    for prefix in prefixes:
        names = prefix + suffixe + ','

    return names


def prime_integer_summation() -> int:

    return 0


def factorial(number: int) -> int:
    factorial_nbr = 1
    for i in range(2, number+1):
        factorial_nbr *= i
    return factorial_nbr


def use_continue() -> None:
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    result = []
    for group in groups:
        if len(group) < 10 and len(group) > 3:
            result.append(True)
        if 25 in group:
            result.append(True)
            break
        if 18 not in group:
            result.append(True)
        elif group
    

                
    return result


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
