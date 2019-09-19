#ARRAYS
# = REEKSEN van (verschillende) datatypes

reeksGetallen = []
som=0
aantalGetallen = int(input("Hoeveel getallen wenst u in te geven?"))

for x in range(0, aantalGetallen):
	reeksGetallen.append(int(input("Geef een getal in:")))

print(reeksGetallen)
print(reeksGetallen[2])

for x in range(0, aantalGetallen):	
	som = som + reeksGetallen[x]
	print(som)

	
print("De som van de getallen is: ", som)


#som += reeksGetallen[x]