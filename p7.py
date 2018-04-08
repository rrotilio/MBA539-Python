validLength = False

while not validLength:
	newInput = (input("Enter filename: "))
	newList = newInput.split('.')
	if (len(newList) == 2):
		print("Your file type is .",newList[1])
		validLength = True
	else:
		print("Not a valid filename.  Try again")