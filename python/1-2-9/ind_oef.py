#priemgetallen

afdrukOpscherm =""
getal = int(input("geef een eindgetal in:"))
 
for x in range(2, getal):
    for y in range(2, x):
        if x % y == 0:
            print(x,'=',y,'*',x/y)
            break
    else:
        print(x,'is een priemgetal')
        afdrukOpscherm = afdrukOpscherm + str(x) + ","
 
print(afdrukOpscherm[:-1])
	