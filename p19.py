
emptyInput=False
#add empty input check
#maybe add int/float check

varFact = str(input("Tell me a cool fact: "))

while (varFact.endswith(".")) or (varFact.endswith("!")) or (varFact.endswith("?")):
		varFact = varFact [:-1]
if (varFact.startswith("Is")) or (varFact.startswith("is")):	
	print("Wow, " + varFact + "?  That's cool!")
else:
	print("Wow, is " + varFact + "?  That's cool!")
