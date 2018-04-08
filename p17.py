from decimal import *
#import locale

#locale.setlocale(locale.LC_ALL, 'en_US')
#locale.format("%d", 1255000, grouping=True)

#getcontext().prec = 10

validNum = False


def doMath(var1):
	diffM = abs(1000 - var1)
	diffMM = abs(2000 - var1)
	if (diffM <= 100 or diffMM <= 100):
		print("Your number is with 100 of 1,000 or 2,000.")
		if(diffM <= 100):
			print("Your number is",diffM,"away from 1,000.")
		elif(diffMM <= 100):
			print("Your number is",diffMM,"away from 2,000.")
	else:
		print("Your number is not within 100 of 1,000 or 2,000.")
		if(diffM < diffMM):
			print("It is closer to 1,000.\nIt is",diffM,"away.")
		elif (diffMM < diffM):
			print("It is closer to 2,000.\nIt is",format(diffMM,","),"away.")
		else: 
			print("It is",diffM,"from both 1,000 and 2,000.\nIf the difference isn't 500, then you broke math.")
	
print("Is your number within 100 of 1,000 or 2,000?")
while not validNum:
	try:
		varNum = Decimal(input("What is your number?: "))
		validNum = True
	except:
		print("I don't recognize your number. Try again.")


doMath (varNum)
#varTest = Decimal(200000)
#print(format(varTest,','))