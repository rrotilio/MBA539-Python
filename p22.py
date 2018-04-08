newInput = input("Enter items that you want to add to a list (seperated by commas): ")
newList = newInput.split(',')

print("Your list is: ",newList)

print("The number 4 is in your list "+str(newList.count('4'))+" times.")