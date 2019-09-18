hoeveelGetallen = int(input("Hoeveel getallen?"))
som = 0

for teller in range(1, hoeveelGetallen+1):
	print("Geef getal ", teller, " in:")
	getal = int(input())
	som = som + getal

print("De totale som is ", som)


	