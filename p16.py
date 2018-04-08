from decimal import *


#getcontext().prec = 10

validNum = False


def doMath(var1):
	diff = 17 - var1
	if (diff == 0):
		print("The numbers are the same!")
	elif (diff>0):
		print("17 is",diff,"bigger than your number")
	elif (diff<0):
		absDiff = abs(diff)
		double = abs(absDiff) * 2
		print("You picked a number higher than 17.\nYour number is",absDiff,"larger than 17.\nTwice that is",double,".")

print("Let's find out how much bigger 17 is than your number")
while not validNum:
	try:
		varNum = Decimal(input("What is your number?: "))
		validNum = True
	except:
		print("I don't recognize your number. Try again.")


doMath (varNum)