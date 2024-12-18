#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def format_bill_total(data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	prix_sous_total = 0
	for achat in data:
		prix_sous_total += achat[INDEX_QUANTITY] * achat[INDEX_PRICE]
		
	taxes = prix_sous_total*0.15
	prix_total = prix_sous_total + taxes

	resultat = f"SOUS TOTAL {prix_sous_total:>16.2f}"
	resultat += f"\n" + f"TAXES      {taxes:>16.2f}"
	resultat += f"\n" + f"TOTAL      {prix_total:>16.2f}"

	



	return resultat

def format_bill_items(data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	
	return ""

def format_number(number, num_decimal_digits):
	return ""

def get_triangle(num_rows):
	return ""


if __name__ == "__main__":
	purchases = [
		("chaise ergonomique", 1, 399.99),
		("g-fuel", 69, 35.99),
		("blue screen", 2, 39.99)
	]
	print(format_bill_items(purchases).strip())
	print("- - - - - - - - - - - - - - - - - - -")
	print(format_bill_total(purchases).strip())

	print("\n------------------")

	print(format_number(-1420069.0678, 2))

	print("\n------------------")

	print(get_triangle(2))
	print(get_triangle(5))
