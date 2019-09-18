aantalSterren = int(input("Geef het max aantal sterren"))
ster="*"
afdrukOpScherm = ""

for x in range(0, aantalSterren, 1):
	afdrukOpScherm = afdrukOpScherm + ster
	print(afdrukOpScherm)

for x in range(0,aantalSterren,1):
	print(afdrukOpScherm[aantalSterren:x:-1])
