import calendar

validYear = False
validMonth = False

def getCal(varYear,varMonth):
	c = calendar.TextCalendar(6)
	print(c.formatmonth(varYear,varMonth))

while not validYear:
	try:
		varYear = int(input("What year do you want a calendar for?: "))
		if(varYear <= 0):
			print("Please select positive number")
		else:
			#print("got it"). #debug making it to valid toggle
			validYear = True
	except:
		print("I do not recognize that year.  Please use whole numbers only.")

while not validMonth:
	try:
		varMonth = int(input("What month do you want a calendar for? (1-12): "))
		if(varMonth <= 0 or varMonth > 12):
			print("Please select a whole number between 1 and 12")
		else:
			validMonth = True
	except:
		print("I do not recognize that month.  Please use whole numbers only.")
#print(varYear,"\n",varMonth,"\n") #debug inputs are as expected

#getCal(2018,12)

getCal (varYear,varMonth)