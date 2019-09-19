#priemgetallen

getal = int(input("Geef een getal in groter dan nul:"))
afdrukOpscherm=""
teller= 0

for x in range(1, getal):
	if(x%2 != 0):
		teller = teller + 1
		if(teller <=2):
			afdrukOpscherm = afdrukOpscherm + str(x) + ","
	teller = 0
print(afdrukOpscherm[:-1])