#!/usr/bin/env python

import math


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return 0

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	# v1[0] et v2[0] pour accéder au X
	# v1[1] et v2[1] pour accéder au Y
	pass

def point_in_circle(point, circle_center, circle_radius):
	# TODO: Retourner vrai si le point est à l'intérieur du cercle, faux sinon.
	# point[0] et circle_center[0] pour accéder au X
	# point[1] et circle_center[1] pour accéder au Y
	pass

def cash(valeur):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$, 25¢, 10¢ et 5¢ à remettre pour représenter la valeur. Il faut arrondir à la pièce de 5¢ près. Il faut remplir les variables twenties, tens, fives, ones, quarters, dimes et nickels avec le quantité de chaque dénomination.
	# Définition des unités pour les dollars et les cents
    unites_dollars = [20, 10, 5, 1]
    unites_cents = [25, 10, 5]

    # Séparer la valeur en dollars et en cents
    dollars = int(valeur)
    cents = int(round(valeur % 1.0 * 100 / 5) * 5)

    # Calculer le nombre de chaque unité de dollars
    resultat = []
    for unite in unites_dollars:
        quantite, dollars = divmod(dollars, unite)
        resultat.append(quantite)

    # Calculer le nombre de chaque unité de cents
    for unite in unites_cents:
        quantite, cents = divmod(cents, unite)
        resultat.append(quantite)

    return tuple(resultat)
	

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres.
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		pass
	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		pass
	return result


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(point_in_circle([-1, 1], [1, -1], 2))
	print(cash(137.38))
	print(format_base(-42, 16, "0123456789ABCDEF"))
