som = 0

ctlGetal = int(input("Getal?"))
test = int(input("Geef test in"))
while ctlGetal >=0 or test == 5 :
	som += ctlGetal
	ctlGetal = int(input("Getal?"))
	test = int(input("Geef test in:"))
	if ctlGetal < 0:
		print("De som is:",som)