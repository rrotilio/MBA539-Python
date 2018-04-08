from decimal import *


validNum1 = False
validNum2 = False
validNum3 = False

def doMath(var1,var2,var3):
	sum1 = var1 + var2 + var3
	print("The sum of your numbers is "+str(sum1)+".")
	if (var1 == var2 and var2 == var3):
		triple = sum1 * 3
		print("You really like the number "+str(var1)+"!")
		print("Triple the sum of your numbers is ",str(triple)+".")
	
	
print("I can add three numbers for you.")

while not validNum1:
	try:
		varNum1 = Decimal(input("What is your first number?: "))
		validNum1 = True
	except:
		print("I don't recognize your number. Try again.")

while not validNum2:
	try:
		varNum2 = Decimal(input("What is your first number?: "))
		validNum2 = True
	except:
		print("I don't recognize your number. Try again.")

while not validNum3:
	try:
		varNum3 = Decimal(input("What is your first number?: "))
		validNum3 = True
	except:
		print("I don't recognize your number. Try again.")


doMath (varNum1,varNum2,varNum3)
