import math

validInput = False
tryAgain = True
tryAgainAns = "y"

def area (num1):
	print("Calculating...")
	varArea = math.pow(num1,2) * math.pi
	print "The area is ", varArea

#while tryAgain:
print("I will calculate the area of a circle for you.")
while not validInput:
	try:
		varRad = int(input(("What is the radius of the circle?: ")))
		validInput = True
	except ValueError:
		print("Invalid input.  Please try again.")
	except SyntaxError:
		print("Invalid input.  Please try again.")
	except NameError:
		print("Invalid input.  Please try again.")
	except:
		print("Unknown error")
area(varRad)
	#tryAgainAns = input("Would you like to calculate the area of another"
						#" cirlce? (y for yes, any other key to exit): ")
	#if(tryAgainAns != 'y'):
		#TryAgain = False





