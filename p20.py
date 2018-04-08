validInt = False

def doRepeat (str1,int1):
	i = 0
	while (i < int1):
		print(str1)
		i = i + 1

print("I like to repeat things.")

varStr = str(input("What do you want me to repeat?: "))

while not validInt:
	try:
		varInt = int(input("How many times should I repeat it?: "))
		if(varInt < 0):
			print("I can't repeat something negative times! Choose a positve number")
		else:
			validInt = True
	except:
		print("Whole numbers only please.  Try again.")

doRepeat(varStr,varInt)