getal = int(input("Geef een getal in:"))
afdrukGetal = 1
afdrukOpScherm= ""

for x in range(1, getal+1, 1):
	afdrukGetal = afdrukGetal * 2
	if(afdrukGetal <= getal):
		afdrukOpScherm=afdrukOpScherm + str(afdrukGetal) + ","

print(afdrukOpScherm[:-1])



0:Tom
1:45
2:m

Naam:Tom
Leeftijd:45
geslacht:m

persoon[0]
persoon[Naam]

persoon.naam