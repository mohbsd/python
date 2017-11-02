### creation d'une liste de film a agrementer


# creation des variables
add_movies = 'y'
movies_list = []
# creation de la boucle
while add_movies == 'y':
	movies_to_register = raw_input('Please enter a movie name : ')
	
	if movies_to_register.lower() in [movie[0].lower() for movie in movies_list]:
		print ('the movie '"'{0}'"' is already into the list' .format(movies_to_register))
	else:
		note = raw_input('enter a value for it : ')
		movies_list.append((movies_to_register, note))

	add_movies = raw_input('Would you like to add another movie y/n : ' )
	print('')

movies_list.sort()
print(movies_list)


