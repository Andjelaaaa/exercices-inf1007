#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_first_part_of_name(name):
	premier_nom = name.split("-")[0]
	premier_nom_modif = premier_nom[0].upper() + premier_nom[1:].lower()
	return f"Bonjour {premier_nom_modif}"

def get_random_sentence(animals, adjectives, fruits):
	animal = animals[random.randrange(len(animals))]
	adjectif = adjectives[random.randrange(len(adjectives))]
	fruit = fruits[random.randrange(len(fruits))]
	return f"Aujourd'hui, j'ai vu un {animal}"

def format_date(year, month, day, hours, minutes, seconds):
	
	return ""

def encrypt(text, shift):
	return ""

def decrypt(encrypted_text, shift):
	return ""


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))

	print(format_date(1970, 1, 12, 12, 3, 45.6789))

	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
