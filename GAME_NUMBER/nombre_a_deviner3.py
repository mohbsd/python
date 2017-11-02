from random import randint

nombre_a_deviner =randint(1,100)
print(nombre_a_deviner)

premier_essai=input('Entrez un nombre (essai 1):')

if premier_essai==nombre_a_deviner:
	print('Bravo')
elif premier_essai < nombre_a_deviner:
	print('le nombre a deviner est superieur a :' + str(premier_essai))
else:
	print('le nombre a deviner est inferieur a :' + str(premier_essai))
print('end of the game')