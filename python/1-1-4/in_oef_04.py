minLeeftijd = 18
geboorteJaar = int(input("Geboortejaar:"))
lopendeJaar = int(input("LopendeJaar:"))
leeftijd = lopendeJaar - geboorteJaar

if(leeftijd >= 18):
	print("Vanaf nu mag, kan en beslis ik alles...")
elif(leeftijd < 0):
	print("Dit is een negatief getal, mag niet")
else:
	print("Gelukkig zijn mijn ouders er nog...")
