print(abs.__doc__)

for i in range (1):
	file = input('Enter the function name that you want help on:')
	function = help(file)
	print(function)
	
	#can't get to end when running in terminal
