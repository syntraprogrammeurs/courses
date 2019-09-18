getal1 = input("Geef getal 1 in:")
getal2 = int(input("Geef getal 2 in:"))

if(int(getal1) > getal2):

	product = int(getal1) * getal2
	print("Product:", product)

	som = int(getal1) + getal2
	print("Som:", som)

	verschil = int(getal1) - getal2
	print("Verschil:", verschil)

	quotient = int(getal1) / getal2
	print("Quotient:", quotient)
else:
	print("error, getal1 moet groter zijn dan getal2")