getal = int(input("Geef een getal in:"))
afdrukGetal = 1
afdrukOpScherm= ""

for x in range(1, getal+1, 1):
	afdrukGetal = afdrukGetal * 2
	if(afdrukGetal <= getal):
		afdrukOpScherm=afdrukOpScherm + str(afdrukGetal) + ","

print(afdrukOpScherm[:-1])