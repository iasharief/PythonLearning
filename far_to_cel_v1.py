import sys
starting_which_one = str(input("Type 'c' if you want to convert Celsius to Fahrenheit, and type 'f' if you want to convert Fahrenheit to Celsius:"))

if starting_which_one != 'c' or starting_which_one != 'f':
	print ("You are not paying attention, you knucklehead!!!")
	sys.exit()

if starting_which_one == 'f':
	far = float(input('Fahrenheit number: ' ))
	cel = 5 / 9 * (far - 32)
	print('The number in celsius is {:.2f}.'.format(cel))
	
if starting_which_one == 'c':
	far2 = float(input('Celsius number:'))
	cel2 = (far2 * 1.8) + 32
	print('The number in fahrenheit is: {:.2f}.'.format(cel2))