import datetime
#from datetime import timedelta

validYear1 = False
validMonth1 = False
validDay1 = False
validYear2 = False
validMonth2 = False
validDay2 = False



def daysBtwDt(day1,day2):
	varDiff = abs(((day2-day1).days))
	#varDiff = datetime.timedelta(day2 - day1)
	#varDiff = timedelta.resolution (days = 1)
	print("There are",varDiff,"days between",day1,"and",day2,".")




while not validYear1:
	try:
		year1 = int(input("What is year of earlier date?: "))
		if (year1 <= 0):
			print("Enter positive number")
		else:
			validYear1 = True
	except:
		print("Unrecognized format, try again.")

while not validMonth1:
	try:
		month1 = int(input("What is month of the earlier date? (1-12): "))
		if (month1 <= 0 or month1 > 12):
			print("Enter number betweeen 1-12")
		else:
			validMonth1 = True
	except:
		print("Unrecognized format, try again.")

while not validDay1:
	try:
		day1 = int(input("What day of the month is earlier date?: "))
		if(day1 <= 0):
			print("Enter valid date")
		elif (month1 == 2 and day1 > 28):
			print("Enter valid date")
		elif ((month1 == 4  or month1 == 6  or month1 == 9 or month1 ==11) and day1 > 30):
			print("Enter valid date")
		elif (day1 > 31):
			print("Enter valid date")
		else:
			validDay1 = True
	except:
		print("Unrecognized format, try again.")

while not validYear2:
	try:
		year2 = int(input("What is year of later date?: "))
		if (year2 <= 0):
			print("Enter positive number")
		else:
			validYear2 = True
	except:
		print("Unrecognized format, try again.")

while not validMonth2:
	try:
		month2 = int(input("What is month of the later date? (1-12): "))
		if (month2 <= 0 or month2 > 12):
			print("Enter number betweeen 1-12")
		else:
			validMonth2 = True
	except:
		print("Unrecognized format, try again.")

while not validDay2:
	try:
		day2 = int(input("What day of the month is later date?: "))
		if(day2 <= 0):
			print("Enter valid date")
		elif (month2 == 2 and day2 > 28):
			print("Enter valid date")
		elif ((month2 == 4 or month2 == 6 or month2 == 9 or month2 ==11) and day2 > 30):
			print("Enter valid date")
		elif (day2 > 31):
			print("Enter valid date")
		else:
			validDay2 = True
	except:
		print("Unrecognized format, try again.")

date1 = datetime.date (year1,month1,day1)
date2 = datetime.date (year2,month2,day2)

daysBtwDt (date1,date2)



#daysBtwDt(100,80)