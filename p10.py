isInt = False

def add (num1):
	num1str = str(num1)
	double = int(num1str+num1str)
	triple = int(num1str+num1str+num1str)
	newSum =  num1 + double + triple
	print (num1,"+",double,"+",triple,"=",newSum)

while not isInt:
	try:
		var1 = int(input("Enter a positive one digit number: "))
		if(var1 < 0):
			print("Positive number please.  Try again.")
		elif(var1 > 9):
			print("Single digit number please.  Try again.")
		else:
			isInt = True
	except:
		print("Not a recognized number.  Try again.")

add(var1)