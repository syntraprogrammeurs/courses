leeftijd = int(input("Leeftijd?"))
if(leeftijd >= 18):
	aantalVakjes = int(input("Aantalvakjes?"))
	if(aantalVakjes == 12):
		print("20 euro")
	elif(aantalVakjes == 10):
		print("18 euro")
	elif(aantalVakjes == 8):
		print("16 euro")
	elif(aantalVakjes == 6):
		print("12 euro")
	elif(aantalVakjes == 4):
		print("8 euro")
	elif(aantalVakjes == 2):
		print("4 euro")
	else:
		print("niet correct aantal vakjes ingegeven")
else:
	print("niet oud genoeg")