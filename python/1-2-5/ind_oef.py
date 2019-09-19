afdrukOpScherm= ""
for x in range(0,100,1):
	if(x < 10):
		afdrukOpScherm = afdrukOpScherm + "0" + str(x) + ","
	else:
		afdrukOpScherm = afdrukOpScherm + str(x) + ","

print(afdrukOpScherm[:-1])