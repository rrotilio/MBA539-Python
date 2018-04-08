import time

int1 = 0

listInts = [1,3,6,7,12,15,20,22,25]

def guess(int1):
	validInt = False
	while not validInt:
		try:
			int1 = int(input("Guess a number: "))
			if(int1 <= 0 or int1 > 25):
				print("Choose a number between 1 and 25")
			else:
				validInt = True
				print("Checking list....")
				time.sleep(1)
				return int1
				
		except:
			print("I don't understand.  Try again.")

def isNum (int1):
	listInts = [1,3,6,7,12,15,20,22,25]
	i = 0
	while (i < 3):
		int1 = guess(int1)
		if int1 in listInts:
			print("You Win!")
			i = 3
		elif (i < 2):
			i = i + 1
			print("Nope, guess again you have " + str(3 - i) + " guesses left.")
		else:
			print ("You lose!")
			i = i + 1

print("Can you guess the numbers on my list (1-25)?")


isNum(int1)

