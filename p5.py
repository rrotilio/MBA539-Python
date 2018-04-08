def reverseString (string):
    return string[::-1]
varFirstName = ""
varLastName = ""
varFirstName = input("What is your first name?: ")
varLastName = input("What is your last name?: ")
print ("Your name reversed is ",varLastName,varFirstName)
print ("Or if you want to get real crazy, it is",
	reverseString(varLastName),reverseString(varFirstName))