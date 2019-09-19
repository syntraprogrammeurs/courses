# 2/2 = 1
# 2%2 = 0 = REST VAN DE DELING

#de gebruiker heeft een getal ingegeven: 7

getal = int(input("Geef een getal groter dan nul in"))

for x in range(0,getal+1):
	rest = x%2
	if(rest == 0):
		print(x)
