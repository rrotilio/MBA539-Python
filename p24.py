validStr = False

listVowels = ['a','e','i','o','u']
listCons = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']

def isVowel (str1):
	if (str1.lower() == 'y'):
		print(str1.upper() + " is SOMETIMES a vowel.")
	elif (str1.lower() in listVowels):
		print(str1.upper() + " is a vowel.")
	else:
		print(str1.upper() + " is a consonant.")

while not validStr:
	try:
		varStr = str(input("Pick a letter: "))
		if(len(varStr) <= 0):
			print("Pick a letter: ")
		elif (len(varStr) > 1):
			print("Please pick only one letter")
		elif (varStr.lower() in listVowels or varStr.lower() in listCons or varStr.lower() == 'y'):
			validStr = True
		else:
			print("I don't recognize that letter")
	except:
		print("I don't understand.  Try again.")

isVowel(varStr)
