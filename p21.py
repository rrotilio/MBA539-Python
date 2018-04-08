validInt = False

def isOdd (int1):
	if (int1 == 0):
		print ("You entered the number zero.")
	elif (abs(int1 % 2) == 0):
		print(str(int1) + " is even.")
	else:
		print (str(int1) + " is odd.")

print("I can tell you if a number is odd or even.")

while not validInt:
	try:
		varInt = int(input("What is your number?: "))
		validInt = True
	except:
		print("Whole numbers only please.  Try again.")

isOdd(varInt)