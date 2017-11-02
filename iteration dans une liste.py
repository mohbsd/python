liste = ['oeuf', 'tomate', 'concombre']
for i in liste:
	print('Vous avez un ingredient qui se nomme : {0}'.format(i))
print ('mais ajoutons un ingredient a cette superbe liste')
liste = liste + ['fromage']
liste.sort()
print(liste)
liste.reverse()
print(liste) *100