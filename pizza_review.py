# we create the variable to continue the porcess
continuing = "y"
# we create an empty pizza list to be fulfilled
pizza_list = []
# creation of the loop for adding more than one pizza
while continuing == "y":
	# we save the pizza name 
	add_a_pizza = raw_input('Please enter a good pizza : ')
	# we verify that the pizza is not present in the list with a condition
	if add_a_pizza.lower() in [pizza[0].lower() for pizza in pizza_list]:
		print ('{0} is already in the list' .format(add_a_pizza))
	else:
		# if the pizza is not in the list, we add it
		# we ask the customer to enter a value for it btw 1 & 5
		note = raw_input('Enter a rating of 5 for this pizza :')
		pizza_list.append((add_a_pizza, note))

	# we ask if the customer wants to add more pizzas
	continuing = raw_input('Would you like to add another pizza ? y/n :' )
	print('')

# we sort the list and display to the screen
pizza_list.sort()	
print(pizza_list)
