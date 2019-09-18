minLeeftijd = 18
geboorteJaar = int(input("Geboortejaar:"))
lopendeJaar = int(input("LopendeJaar:"))
leeftijd = lopendeJaar - geboorteJaar
if(leeftijd >= 18):
	print("Vanaf nu mag, kan en beslis ik alles...")
else:
	print("Gelukkig zijn mijn ouders er nog...")
