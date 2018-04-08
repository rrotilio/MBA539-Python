validInt = False

def doRepeat (str1,int1):
	if (len(str1) > 2):
		newStr = (str1[0:2])
		print(newStr * int1)
	else:
		print(str1 * int1)

varStr = str(input("Tell me a statement: "))

while not validInt:
	try:
		varInt = int(input("Pick a positive number: "))
		if(varInt < 0):
			print("Choose a positve number")
		else:
			validInt = True
	except:
		print("Whole numbers only please.  Try again.")

doRepeat(varStr,varInt)
#string1 = str("this is my string")
#print(string1 [0:5])